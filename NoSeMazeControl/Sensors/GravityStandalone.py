import csv
import time
from pathlib import Path
import serial
from datetime import datetime
import threading
from queue import Queue

class GravitySensor:
    """
    Class to handle measurement reading and saving as CSV.
    """
    
    def __init__(self, com_port_number):
        """
        Initializes the measurement object and creates a folder for CSVs if it doesn't exist.
        """
        self.timestamp = time.strftime("%y%m%d_%H%M", time.localtime())
        self.measurement_queue = Queue()
        self.running = True
        outputfolder = "csv"
        self.gravity_file =  ["NH3", ["Timestamp", "NH3[ppm]"]]
        self.com_port = f"COM{com_port_number}"  # Prepend 'COM' to the port number
        self.ser = None  # Serial connection will be initialized later

        # Create output directory
        path_name = Path.cwd() / outputfolder / "gravity_NH3"
        if not path_name.exists():
            path_name.mkdir(parents=True)

        # Create the measurement CSV file
        self.csv_file_path = path_name / "gravity_nh3_standalone.csv"
        self._initialize_csv()

    def _initialize_csv(self):
        """
        Initializes the CSV file with headers if it does not exist.
        """
        file = self.gravity_file
        if not self.csv_file_path.exists():  # Check if the CSV file already exists
            try:
                with open(self.csv_file_path, "w", newline="") as csvfile:
                    output = csv.writer(csvfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    output.writerow(file[1])  # Assuming file[1] contains headers
                print(f"Created CSV file: {self.csv_file_path}")
            except Exception as e:
                print(f"Could not create file: {e}")
        else:
            print(f"CSV file already exists: {self.csv_file_path}")

    def write_csv_row_to_file(self, csv_row: list):
        """
        Method to write one row into the CSV file.
        """
        try:
            with open(self.csv_file_path, "a", newline="") as csvfile:
                output = csv.writer(csvfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                output.writerow(csv_row)
        except Exception as e:
            print(f"Error writing to CSV: {e}")

    def open_serial_connection(self):
        """
        Attempts to open the serial connection.
        """
        try:
            self.ser = serial.Serial(self.com_port, 115200, timeout=1)
            print(f"Opened serial connection on {self.com_port}")
        except serial.serialutil.SerialException:
            print(f"Could not open port [{self.com_port}] with gravity sensor. Retrying...")
            self.ser = None
            
    def meas_loop(self):
        """
        Method to receive measurements and write them into the CSV file.
        """
        while self.running:
            if not self.ser:
                self.open_serial_connection()
            time.sleep(5)  # Wait for 1 second before the next measurement


            if self.ser:
                try:
                    # Send the command 'measure'
                    send_buf = 'measure\n'
                    self.ser.write(send_buf.encode())
                    self.ser.flush()

                    # Wait for the measurement
                    measurement = self.ser.readline().decode('utf-8').rstrip()
                    if measurement:
                        try:
                            measurement = float(measurement)
                        except ValueError:
                            print("This data is not a measurement")
                            pass
                        else:
                            timestamp = datetime.now().timestamp()
                            print(f"Received measurement: {measurement}")
                            self.measurement_queue.put((timestamp, measurement))

                    time.sleep(5)  # Wait for 5 seconds before the next measurement

                except serial.SerialException:
                    print("Serial connection lost. Attempting to reconnect...")
                    self.ser.close()  # Close the connection to reopen it later
                    self.ser = None  # Set to None to trigger reconnection

        # Close the serial port when done
        if self.ser:
            self.ser.close()

    def save_measurements(self):
        """
        Continuously save measurements from the queue to the CSV file.
        """
        while self.running:
            while not self.measurement_queue.empty():
                timestamp, measurement = self.measurement_queue.get()
                self.write_csv_row_to_file([timestamp, measurement])

    def start(self):
        """
        Start the measurement loop and saving thread.
        """
        self.measure_thread = threading.Thread(target=self.meas_loop)
        self.save_thread = threading.Thread(target=self.save_measurements)

        self.measure_thread.start()
        self.save_thread.start()

    def stop(self):
        """
        Stop the measurement and saving threads.
        """
        self.running = False
        self.measure_thread.join()
        self.save_thread.join()

if __name__ == "__main__":
    # Ask the user for the COM port number (without 'COM')
    com_port_number = input("Enter the COM port number (e.g., 3 for COM3): ")
    
    # Initialize the GravitySensor with the specified COM port
    sensor = GravitySensor(com_port_number)
    try:
        sensor.start()
        while True:
            time.sleep(10)  # Keep the main thread alive
    except KeyboardInterrupt:
        print("Stopping measurement...")
        sensor.stop()
        print("Measurement stopped.")
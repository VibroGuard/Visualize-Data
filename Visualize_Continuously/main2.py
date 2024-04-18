# import serial
# import serial.tools.list_ports
#
# from visualize import *
#
#
# def find_arduino(port=None):
#     """Get the name of the port that is connected to Arduino."""
#     if port is None:
#         ports = serial.tools.list_ports.comports()
#         for p in ports:
#             if p.manufacturer is not None and "Arduino" in p.manufacturer:
#                 port = p.device
#     return port
#
#
# def fill_buffer(buffer, num_samples):
#     i = 0
#     temp_buffer = []
#
#     while i < num_samples:
#         try:
#             value = float(ser.readline())
#         except:
#             value = 0.0
#         temp_buffer.append(value)
#         i += 1
#
#     if buffer.casefold() == "x":
#         x_data.clear()
#         x_data.extend(temp_buffer)
#     elif buffer.casefold() == "y":
#         y_data.clear()
#         y_data.extend(temp_buffer)
#     elif buffer.casefold() == "z":
#         z_data.clear()
#         z_data.extend(temp_buffer)
#
#
# port = find_arduino()
#
# if (port is not None):
#     ser = serial.Serial()
#     ser.baudrate = 115200
#     ser.port = port
#     ser.open()
#     if ser.is_open:
#         print("Serial port: " + port + " is opened.")
#     else:
#         print("Serial port: " + port + " cannot be opened.")
#
#     num_samples = 512  # This should match with the number of samples taken by the MCU.
#     sampling_frequency = 100
#
#     x_data = [0] * num_samples
#     y_data = [0] * num_samples
#     z_data = [0] * num_samples
#
#     fig, axs = plt.subplots(2, 3, figsize=(15, 5))
#
#     while True:
#         received_data = str(ser.readline())[2:-5].casefold()
#         # print(received_data)
#         if received_data == "x":
#             fill_buffer("x", num_samples)
#         elif received_data == "y":
#             fill_buffer("y", num_samples)
#         elif received_data == "z":
#             fill_buffer("z", num_samples)
#
#         print(x_data)
#         print(y_data)
#         print(z_data)
#         #
#         fft_ij_x, fft_mag_x = fft_data(x_data)
#         fft_ij_y, fft_mag_y = fft_data(y_data)
#         fft_ij_z, fft_mag_z = fft_data(z_data)
#         # #     print(fft_mag_x)
#         # #     print(fft_mag_y)
#         # #     print(fft_mag_z)
#         #
#
#         # if received_data is not None:
#         visualize_data(x_data, y_data, z_data, sampling_frequency, "time", fig, axs)
#         #
#         visualize_data(fft_mag_x, fft_mag_y, fft_mag_z, sampling_frequency, "frequency", fig, axs)
#
#             # received_data = None
# else:
#     print("Port not found.")
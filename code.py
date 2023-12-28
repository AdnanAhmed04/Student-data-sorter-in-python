{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f5e8f14c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data has been sorted and saved to 'sorted_student_roll_numbers.txt'.\n"
     ]
    }
   ],
   "source": [
    "def bubble_sort(arr):\n",
    "    n = len(arr)\n",
    "\n",
    "    for i in range(n - 1):\n",
    "        for j in range(0, n - i - 1):\n",
    "            if arr[j] > arr[j + 1]:\n",
    "                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n",
    "\n",
    "def read_data_from_file(file_path):\n",
    "    with open('my_text.txt', 'r') as file:\n",
    "        data = file.readlines()\n",
    "    return [int(roll_no.strip()) for roll_no in data]\n",
    "\n",
    "def write_data_to_file(file_path, data):\n",
    "    with open(file_path, 'w') as file:\n",
    "        for roll_no in data:\n",
    "            file.write(str(roll_no) + '\\n')\n",
    "\n",
    "# Input and output file paths\n",
    "input_file_path = 'student_roll_numbers.txt'\n",
    "output_file_path = 'sorted_student_roll_numbers.txt'\n",
    "\n",
    "# Read data from the input file\n",
    "roll_numbers = read_data_from_file(input_file_path)\n",
    "\n",
    "# Sort the data using bubble sort\n",
    "bubble_sort(roll_numbers)\n",
    "\n",
    "# Write the sorted data to the output file\n",
    "write_data_to_file(output_file_path, roll_numbers)\n",
    "\n",
    "print(f\"Data has been sorted and saved to '{output_file_path}'.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1835f038",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f788a504",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import filedialog\n",
    "\n",
    "def bubble_sort(arr):\n",
    "    n = len(arr)\n",
    "    for i in range(n - 1):\n",
    "        for j in range(0, n - i - 1):\n",
    "            if arr[j] > arr[j + 1]:\n",
    "                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n",
    "def read_data_from_file(file_path):\n",
    "    with open(file_path, 'r') as file:\n",
    "        data = file.readlines()\n",
    "    return [int(roll_no.strip()) for roll_no in data]\n",
    "def write_data_to_file(file_path, data):\n",
    "    with open(file_path, 'w') as file:\n",
    "        for roll_no in data:\n",
    "            file.write(str(roll_no) + '\\n')\n",
    "def browse_file():\n",
    "    filename = filedialog.askopenfilename(initialdir=\"/\", title=\"Select File\",\n",
    "                                   filetypes=((\"Text files\", \"*.txt\"), (\"all files\", \"*.*\")))\n",
    "    entry_path.delete(0, tk.END)\n",
    "    entry_path.insert(0, filename)\n",
    "def sort_and_save():\n",
    "    input_file_path = entry_path.get()\n",
    "    output_file_path = 'sorted_student_roll_numbers.txt'\n",
    "    try:\n",
    "        roll_numbers = read_data_from_file(input_file_path)\n",
    "        bubble_sort(roll_numbers)\n",
    "        write_data_to_file(output_file_path, roll_numbers)\n",
    "        result_label.config(text=f\"Data has been sorted and saved to '{output_file_path}'.\")\n",
    "    except Exception as e:\n",
    "        result_label.config(text=f\"Error: {str(e)}\")\n",
    "# Create the main window\n",
    "root = tk.Tk()\n",
    "root.title(\"Student Roll Number data base\")\n",
    "# Create and place widgets\n",
    "label_path = tk.Label(root, text=\"Select Input File:\")\n",
    "label_path.grid(row=0, column=0, padx=10, pady=10)\n",
    "entry_path = tk.Entry(root, width=50)\n",
    "entry_path.grid(row=0, column=1, padx=10, pady=10)\n",
    "button_browse = tk.Button(root, text=\"Browse\", command=browse_file)\n",
    "button_browse.grid(row=0, column=2, padx=10, pady=10)\n",
    "button_sort = tk.Button(root, text=\"Sort and Save\", command=sort_and_save)\n",
    "button_sort.grid(row=1, column=1, pady=10)\n",
    "result_label = tk.Label(root, text=\"\")\n",
    "result_label.grid(row=2, column=0, columnspan=3, pady=10)\n",
    "# Start the Tkinter event loop\n",
    "root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb9812a3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3337ae87",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

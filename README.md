# Invisible WaterMarking 

This repository contains a simple Python script to add a visible watermark to an image using the `Pillow` library.

## Table of Contents

- [Introduction](#Introduction)
- [Features](#Features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

Watermarking is a process of embedding a mark or text into an image to protect it from unauthorized use. This script demonstrates how to add a visible watermark to an image using Python.

## Features

- Add a visible watermark to any image.
- Customize the watermark text.
- Adjust the position and style of the watermark.

## Requirements

- Python 3.x
- `Pillow` library

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/image-watermarking.git
   cd image-watermarking
   
2. **Install the required library:**
   ```sh
   pip install Pillow

## Usage

1. **Prepare your images:**
   - Place your input image in the same directory as the script and name it `input_image.jpg` or update the script with the correct path.

2. **Font file:**
   - Ensure you have a font file (e.g., `arial.ttf`) in the same directory or update the path in the script.

3. **Embed hidden text into the image:**
   - Use the `embed_text()` function in `embedded.py` to embed invisible text in an image.
   - Example usage:

   ```sh
   embed_text('input_image.jpg', 'Invisible Watermarking', './Roboto-Italic.ttf', 30, 30, 'embedded_image.png')

4. **Run `embedded.py` to create an image with embedded text:**

      ```sh
      python watermark.py

5. **Run `extract.py` to reveal the hidden text from the image:**

     ```sh
     python extract.py

## License
MIT License

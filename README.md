# Lossless Compression Project

A comprehensive implementation of lossless compression algorithms for images and audio using Huffman coding, plus machine learning applications for agricultural image classification.

## 🎯 Project Overview

This project implements lossless data compression techniques with three main components:

1. **Image Compression**: RGB channel-wise Huffman coding for lossless image compression
2. **Audio Compression**: Lossless audio compression using similar Huffman coding principles  
3. **Agricultural ML**: Paddy/rice crop classification using deep learning (VGG16-based CNN)

## 🚀 Features

- **Lossless Image Compression**
  - RGB channel separation and independent compression
  - Huffman coding implementation with custom tree construction
  - Compression ratio calculation and performance metrics
  - Support for various image formats via OpenCV

- **Audio Compression**
  - Lossless audio compression using Huffman coding
  - Bit stream generation and decoding
  - MP3 output support

- **Machine Learning Component**
  - Paddy crop classification using CNN
  - Transfer learning with VGG16
  - Image preprocessing and augmentation

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Dependencies

Install the required packages:

```bash
pip install opencv-python numpy matplotlib tensorflow keras pandas
```

For Jupyter notebook support:
```bash
pip install jupyter ipykernel
```

## 🎮 Usage

### Image Compression

Run the image compression script:

```bash
cd image/
python img_c.py
```

When prompted, enter the path to your image file. The script will:
1. Load and display the original image
2. Extract RGB channels
3. Generate histograms and probability distributions
4. Apply Huffman coding compression
5. Calculate compression ratios
6. Save compressed bit streams and decoding tables
7. Demonstrate decompression and reconstruction

**Output files generated:**
- `bit_stream.txt` - Compressed bit stream
- `red_channel_codes.json` - Huffman codes for red channel
- `red_channel_decodes.json` - Decoding table for red channel
- `image_pixel_stream.txt` - Reconstructed pixel data

### Audio Compression

Open and run the Jupyter notebook:

```bash
jupyter notebook "audio compression.ipynb"
```

The notebook provides interactive audio compression with visualizations and performance analysis.

### Agricultural Classification

For the paddy classification model:

```bash
jupyter notebook paddy.ipynb
```

This notebook includes:
- Dataset preparation
- CNN model architecture (VGG16-based)
- Training and validation
- Performance evaluation

## 📁 Project Structure

```
lossless/
├── image/                          # Image compression module
│   ├── img_c.py                   # Main image compression script
│   ├── img_comp.ipynb             # Interactive image compression notebook
│   └── [generated files]          # Compression outputs
├── audio/                          # Audio compression module
│   ├── Untitled.ipynb             # Audio processing notebook
│   └── [audio files]              # Audio compression outputs
├── audio compression.ipynb         # Main audio compression notebook
├── paddy.ipynb                     # Agricultural ML classification
├── *.json                          # Huffman coding tables
├── *_stream.txt                    # Generated bit streams
└── output.mp3                      # Compressed audio output
```

## 🔧 Technical Details

### Huffman Coding Implementation

The project implements a complete Huffman coding system:

1. **Histogram Generation**: Analyzes pixel/sample frequency distributions
2. **Probability Calculation**: Computes probability distributions for optimal encoding
3. **Tree Construction**: Builds Huffman tree using min-heap (priority queue)
4. **Code Generation**: Generates variable-length codes for each symbol
5. **Compression**: Encodes data using generated codes
6. **Decompression**: Reconstructs original data from bit streams

### Key Classes and Functions

- `HeapNode`: Node structure for Huffman tree construction
- `Huffman_Coding`: Main compression class with encoding/decoding methods
- `histogram_array_generator()`: Generates frequency histograms
- `probability_distribution_generator()`: Calculates symbol probabilities
- `compressor()`: Applies Huffman codes to compress data
- `decoder()`: Reconstructs original data from compressed streams

### Compression Performance

The system calculates and displays:
- Original data size (in bits)
- Compressed data size
- Compression ratio
- Space savings percentage

## 🖼️ Example Results

The image compression typically achieves compression ratios between 0.3-0.8 depending on image complexity and color distribution. More uniform images compress better due to higher symbol frequency concentrations.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is available for educational and research purposes. Please refer to the repository for specific licensing terms.

## 🐛 Known Issues

- The image compression script currently expects 1024x1024 images for reconstruction
- Some notebook files are stored using Git LFS for large file handling
- Interactive input prompts in scripts may need modification for automated workflows

## 🔮 Future Enhancements

- Support for arbitrary image dimensions
- Multi-threaded compression for better performance
- GUI interface for easier usage
- Additional compression algorithms (LZW, arithmetic coding)
- Batch processing capabilities
- Performance benchmarking tools

## 📞 Support

For questions, issues, or contributions, please open an issue in the GitHub repository.
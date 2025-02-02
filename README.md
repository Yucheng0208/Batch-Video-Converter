# Batch Video Converter

## Overview
**Batch-Video-Converter.py** is a Python script designed to batch convert video files into different formats. The script supports multiple input formats and allows users to keep or remove audio during conversion. It supports both interactive input mode and command-line parameters.

## Features
- Supports multiple video formats: `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`
- Converts videos to user-specified formats (`mp4`, `avi`, `mov`, `mkv`)
- Option to keep or remove audio
- Batch processing with progress tracking using `tqdm`
- Supports interactive mode and command-line arguments

## Requirements
Ensure you have the following dependencies installed:
```bash
pip install moviepy tqdm
```

## Usage
### Interactive Mode
Run the script without parameters and follow the prompts:
```bash
python Batch-Video-Converter.py
```
The script will prompt for:
- **Input directory**: Directory containing video files
- **Output directory**: Directory for converted files
- **Target format**: Choose from available formats
- **Keep audio**: Decide whether to retain audio in converted files

### Command-Line Mode
Alternatively, you can run the script with parameters:
```bash
python Batch-Video-Converter.py --input_dir path/to/videos --output_dir path/to/output --target_format mp4 --keep_audio
```
- `--input_dir` : Path to input directory containing video files
- `--output_dir` : Path to output directory for converted videos
- `--target_format` : Output format (`mp4`, `avi`, `mov`, `mkv`)
- `--keep_audio` : (Optional) Include this flag to retain audio

### Example
#### Before running the script:
```
/videos
   ├── sample1.avi
   ├── sample2.mov
```
#### Running the script interactively:
```
Enter the input directory containing videos: /videos
Enter the output directory for converted videos (leave blank for default): /converted_videos
Select the target format:
1: mp4
2: avi
3: mov
4: mkv
Enter the format number: 1
Do you want to keep audio in the converted videos? (Y/N, default: N): Y
```
#### Output directory structure:
```
/converted_videos
   ├── sample1.mp4
   ├── sample2.mp4
```

## Code Functionality
1. Reads video files from the input directory
2. Converts each video to the specified format
3. Optionally retains or removes audio
4. Saves converted files in the output directory
5. Uses `tqdm` for progress tracking

## LICENSE
This project is licensed under the [MIT License](LICENSE).

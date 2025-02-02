import os
import argparse
from moviepy.editor import VideoFileClip
from tqdm import tqdm

def convert_videos(input_dir, output_dir, target_format, keep_audio):
    try:
        if not output_dir:
            output_dir = os.path.join(input_dir, "Converted")

        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        supported_formats = ('.mp4', '.avi', '.mov', '.mkv', '.wmv')
        video_files = [f for f in os.listdir(input_dir) if f.lower().endswith(supported_formats)]
        
        if not video_files:
            print("No supported video files found in the selected directory.")
            return

        with tqdm(total=len(video_files), desc="Converting videos", unit="file") as pbar:
            for video_file in video_files:
                input_path = os.path.join(input_dir, video_file)
                output_path = os.path.join(output_dir, os.path.splitext(video_file)[0] + f".{target_format}")

                try:
                    clip = VideoFileClip(input_path)
                    if keep_audio:
                        clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
                    else:
                        clip.write_videofile(output_path, codec="libx264", audio=False)
                    clip.close()
                except Exception as e:
                    print(f"Failed to convert {video_file}: {e}")

                pbar.update(1)

        print("All videos converted successfully!")
    except Exception as e:
        print(f"Failed to process videos: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert videos to a specified format.")
    parser.add_argument("--input_dir", type=str, required=False, help="Input directory containing videos.")
    parser.add_argument("--output_dir", type=str, required=False, help="Output directory for converted videos.")
    parser.add_argument("--target_format", type=str, choices=["mp4", "avi", "mov", "mkv"], required=False, help="Target format for video conversion.")
    parser.add_argument("--keep_audio", action='store_true', help="Keep audio in the converted videos.")
    
    args = parser.parse_args()
    
    if not args.input_dir:
        args.input_dir = input("Enter the input directory containing videos: ").strip()
    if not args.output_dir:
        args.output_dir = input("Enter the output directory for converted videos (leave blank for default): ").strip()
    if not args.target_format:
        print("Select the target format:")
        format_options = {"1": "mp4", "2": "avi", "3": "mov", "4": "mkv"}
        for key, value in format_options.items():
            print(f"{key}: {value}")
        format_choice = input("Enter the format number: ").strip()
        args.target_format = format_options.get(format_choice, "mp4")
    
    if args.keep_audio is None:
        keep_audio_input = input("Do you want to keep audio in the converted videos? (Y/N, default: N): ").strip().lower()
        args.keep_audio = keep_audio_input in ["y", "yes"]

    if not os.path.isdir(args.input_dir):
        print("Invalid input directory.")
    else:
        convert_videos(args.input_dir, args.output_dir, args.target_format, args.keep_audio)

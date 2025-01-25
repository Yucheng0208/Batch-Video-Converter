import os
from moviepy.editor import VideoFileClip
from tqdm import tqdm

def convert_videos_to_mp4(input_dir, output_dir, keep_audio):
    try:
        if not output_dir:
            output_dir = os.path.join(input_dir, "Output")

        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        video_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.wmv', '.mov'))]
        if not video_files:
            print("No WMV or MOV files found in the selected directory.")
            return

        with tqdm(total=len(video_files), desc="Converting videos", unit="file") as pbar:
            for video_file in video_files:
                input_path = os.path.join(input_dir, video_file)
                output_path = os.path.join(output_dir, os.path.splitext(video_file)[0] + ".mp4")

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
    input_dir = input("Enter the input directory containing videos: ").strip()
    output_dir = input("Enter the output directory for converted MP4 videos (leave blank for default): ").strip()
    keep_audio_input = input("Do you want to keep audio in the converted videos? (Y/N, default: N): ").strip().lower()
    keep_audio = keep_audio_input in ["y", "yes"]

    if not os.path.isdir(input_dir):
        print("Invalid input directory.")
    else:
        convert_videos_to_mp4(input_dir, output_dir, keep_audio)

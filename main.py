import os
import concurrent.futures
from tiktok_downloader import snaptik

input_file = 'Input.txt'
output_folder = 'Output'
MAX_THREADS = 10

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def download_tiktok_video(index, url):
    try:
        video = snaptik(url)
        video_id = url.split('/')[-2]
        output_path = os.path.join(output_folder, f"{index+1}_{video_id}.mp4")
        video[0].download(output_path)
    except Exception as e:
        pass

with open(input_file, 'r') as file:
    links = [link.strip() for link in file.readlines() if link.strip()]

def download_videos_in_threads(links):
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        executor.map(download_tiktok_video, range(len(links)), links)

def main():
    download_videos_in_threads(links)
    print("Done")

if __name__ == "__main__":
    main()

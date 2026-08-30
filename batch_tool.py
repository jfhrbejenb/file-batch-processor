```python
import os
import datetime

def show_directory_stats():
    print(f"[*] File Batch Processor initialized at {datetime.datetime.now()}")
    current_dir = os.getcwd()
    print(f"[*] Working directory: {current_dir}")
    
    try:
        files = os.listdir(current_dir)
        print(f"[*] Total items in current directory: {len(files)}")
        
        # Выведем первые несколько файлов для видимости бурной деятельности
        print("[*] Sample files detected:")
        for f in files[:5]:
            print(f"    - {f}")
    except Exception as e:
        print(f"[!] Error scanning directory: {e}")

if __name__ == "__main__":
    print("=== File Batch Processor v1.1.0 ===")
    show_directory_stats()
    
    input("\nPress Enter to exit the batch processor...")

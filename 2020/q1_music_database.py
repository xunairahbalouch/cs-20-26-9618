import csv
import os


def LoadMusicData():
    """Task 1.1: Load and display all records from music.csv"""
    music_file = "music.csv"
    
    if not os.path.exists(music_file):
        print(f"Error: {music_file} not found")
        return []
    
    records = []
    with open(music_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        print(f"Columns: {header}")
        print("-" * 80)
        
        for row in reader:
            records.append(row)
            print(f"TrackID: {row[0]}, Title: {row[1]}, Artist: {row[2]}, "
                  f"Genre: {row[3]}, Duration: {row[4]} seconds")
    
    print(f"\nTotal records: {len(records)}")
    return records


def FindAndDisplayGenre():
    """Task 1.2: Find and display records where genre is 'Pop'"""
    music_file = "music.csv"
    
    if not os.path.exists(music_file):
        print(f"Error: {music_file} not found")
        return
    
    pop_tracks = []
    with open(music_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader:
            if row[3] == 'Pop':
                pop_tracks.append(row)
                print(f"TrackID: {row[0]}, Title: {row[1]}, Artist: {row[2]}")
    
    print(f"\nTotal Pop tracks found: {len(pop_tracks)}")
    return pop_tracks


def FindAndDisplayDuration(limit=240):
    """Task 1.2: Find and display records where duration exceeds specified limit"""
    music_file = "music.csv"
    
    if not os.path.exists(music_file):
        print(f"Error: {music_file} not found")
        return []
    
    long_tracks = []
    with open(music_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader:
            try:
                duration = int(row[4])
                if duration > limit:
                    long_tracks.append(row)
                    print(f"TrackID: {row[0]}, Title: {row[1]}, Duration: {duration}s")
            except ValueError:
                continue
    
    print(f"\nTotal tracks over {limit}s: {len(long_tracks)}")
    return long_tracks


def AddNewRecord(trackid, title, artist, genre, duration):
    """Task 1.3: Add a new record to music.csv"""
    music_file = "music.csv"
    
    with open(music_file, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([trackid, title, artist, genre, duration])
    
    print(f"Record added: {trackid}, {title}, {artist}, {genre}, {duration}")


def UpdateGenre(old_genre, new_genre):
    """Task 1.3: Update all records with old_genre to new_genre"""
    music_file = "music.csv"
    temp_file = "music_temp.csv"
    
    if not os.path.exists(music_file):
        print(f"Error: {music_file} not found")
        return 0
    
    count = 0
    with open(music_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        
        with open(temp_file, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            
            for row in reader:
                if row[3] == old_genre:
                    row[3] = new_genre
                    count += 1
                writer.writerow(row)
    
    os.remove(music_file)
    os.rename(temp_file, music_file)
    
    print(f"Updated {count} records from '{old_genre}' to '{new_genre}'")
    return count


def SearchAndDisplay():
    """Task 1.4: Search by title (partial match, case-insensitive)"""
    music_file = "music.csv"
    
    if not os.path.exists(music_file):
        print(f"Error: {music_file} not found")
        return
    
    search_term = input("Enter title to search: ").strip().lower()
    
    with open(music_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        found = False
        
        for row in reader:
            if search_term in row[1].lower():
                print(f"TrackID: {row[0]}, Title: {row[1]}, Artist: {row[2]}")
                found = True
        
        if not found:
            print("No matching records found.")


def CreatePlaylist():
    """Task 1.4: Create a new playlist with specified duration"""
    music_file = "music.csv"
    playlist_name = input("Enter playlist name: ").strip()
    target_duration = int(input("Enter target duration in seconds: "))
    
    playlist = []
    current_duration = 0
    
    with open(music_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader:
            track_duration = int(row[4])
            if current_duration + track_duration <= target_duration:
                playlist.append(row)
                current_duration += track_duration
    
    with open(f"{playlist_name}.csv", 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for track in playlist:
            writer.writerow(track)
    
    print(f"Playlist '{playlist_name}' created with {len(playlist)} tracks, "
          f"total duration: {current_duration}s")


if __name__ == "__main__":
    print("=" * 80)
    print("Task 1.1: Load and display all records")
    print("=" * 80)
    LoadMusicData()
    
    print("\n" + "=" * 80)
    print("Task 1.2a: Find and display Pop genre tracks")
    print("=" * 80)
    FindAndDisplayGenre()
    
    print("\n" + "=" * 80)
    print("Task 1.2b: Find and display tracks over 240 seconds")
    print("=" * 80)
    FindAndDisplayDuration(240)

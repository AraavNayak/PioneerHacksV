import re
import matplotlib.pyplot as plt

def calculate_wpm(words, timestamp):
    # Count number of words up to the given timestamp
    num_words = sum(len(word) for word in words[:timestamp])
    
    # Calculate words per minute
    if timestamp > 0:
        wpm = (num_words / timestamp) * 60
    else:
        # If timestamp is zero, calculate WPM up to the first second
        wpm = (num_words / 1) * 60
    
    return wpm

def main():
    file_path='output_files/output.txt'
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        transcript = file.read()
    
    # Extract timestamps and words
    timestamps = [int(ts) for ts in re.findall(r'\[(\d+)\]', transcript)]
    words = re.sub(r'\[\d+\]', '', transcript).split()
    
    # Calculate WPM for each timestamp
    wpms = [calculate_wpm(words, ts) for ts in timestamps]
    
    print("Timestamps:", timestamps)

    print("Words per minute for each timestamp:", wpms)
    
    # Plotting the WPM
    plt.plot(timestamps, wpms, marker='o')
    plt.xlabel('Timestamp (seconds)')
    plt.ylabel('WPM')
    plt.title('Words Per Minute Over Time')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
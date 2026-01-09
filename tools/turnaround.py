import json
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys
import os

def process_tickets(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    extracted_records = []
    for item in data.get('items', []): # for each log

        # Component change in log
        for component in item.get('componentChanges', []): 
            results = component.get('changeItems', {}).get('results', [])

            for result in results:

                # Extract JSON data from log
                if result.get('fieldName') == 'Log' and 'changeTo' in result:
                    try:
                        log_data = json.loads(result['changeTo'])
                        extracted_records.append(log_data)
                    except:
                        continue

    if not extracted_records:
        print("No valid data found.")
        return

    # Create data frame
    df = pd.DataFrame(extracted_records)

    # Convert timestamps and points to pandas & add to dataframe
    df['inProgressTriggerTime'] = pd.to_datetime(df['inProgressTriggerTime'], errors='coerce')
    df['doneTriggerTime'] = pd.to_datetime(df['doneTriggerTime'], errors='coerce')
    df['points'] = pd.to_numeric(df.get('storyPoints', 0), errors='coerce').fillna(0)
    
    # Calculate turnaround time from in-progres -> done 
    df['turnaround_hrs'] = (df['doneTriggerTime'] - df['inProgressTriggerTime']).dt.total_seconds() / 3600
    df = df.dropna(subset=['turnaround_hrs']) # drop missing values from turnaround_hrs column
    df['ticket_id'] = df['ticket'].str.split('/').str[-1] # cut the URL to get ticket number

    # --- Plotting ---

    # Main window and first set of axes
    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Left y-axis is story points (estimate)
    color_story_points = '#BDC3C7' 
    ax1.set_xlabel('Ticket Number')
    ax1.set_ylabel('Story Points (Estimate)', color='black', fontsize=12)
    bars = ax1.bar(df['ticket_id'], df['points'], color=color_story_points, alpha=0.5, label='Story Points')
    ax1.tick_params(axis='y', labelcolor='black')

    # Right y-axis for turnaround time
    ax2 = ax1.twinx() # create twin axis for right side
    color_time = '#2E86C1'
    ax2.set_ylabel('Turnaround Time (Hours)', color=color_time, fontsize=12)
    line = ax2.plot(df['ticket_id'], df['turnaround_hrs'], color=color_time, marker='o', linewidth=2, label='Turnaround Time')
    ax2.tick_params(axis='y', labelcolor=color_time)
    

    # Add average line for turnaround time
    avg_hrs = df['turnaround_hrs'].mean()
    ax2.axhline(avg_hrs, color='#E74C3C', linestyle='--', alpha=0.7, label=f'Avg Time: {avg_hrs:.4f}h')

    # Formatting
    plt.title('Ticket Complexity vs. Completion Speed', fontsize=16)
    ax1.set_xticklabels(df['ticket_id'], rotation=45, ha='right')
    
    # Combine legends from both axes
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')

    plt.tight_layout()
    plt.savefig("turnaround_time.png")
    print(f"Report generated: turnaround_time.png")
    print(f"Average Turnaround: {avg_hrs:.4f} hours")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    process_tickets(args.file)
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
    for item in data.get('items', []): 
        for component in item.get('componentChanges', []): 
            results = component.get('changeItems', {}).get('results', [])
            for result in results:
                if result.get('fieldName') == 'Log' and 'changeTo' in result:
                    try:
                        log_data = json.loads(result['changeTo'])
                        extracted_records.append(log_data)
                    except:
                        continue

    if not extracted_records:
        print("No valid data found.")
        return

    df = pd.DataFrame(extracted_records)

    # Clean and convert data
    df['inProgressTriggerTime'] = pd.to_datetime(df['inProgressTriggerTime'], errors='coerce')
    df['doneTriggerTime'] = pd.to_datetime(df['doneTriggerTime'], errors='coerce')
    df['points'] = pd.to_numeric(df['storyPoints'], errors='coerce').fillna(0)
    df['turnaround_hrs'] = (df['doneTriggerTime'] - df['inProgressTriggerTime']).dt.total_seconds() / 3600
    df = df.dropna(subset=['turnaround_hrs'])

    # --- Aggregation ---
    stats_df = df.groupby('points')['turnaround_hrs'].mean().reset_index()
    stats_df = stats_df.sort_values('points')

    # --- Benchmark Data Mapping ---
    # Mapping your provided definitions to hour values
    # Assumes 8-hour work days
    benchmarks = {
        1: 2,    # less than 2 hours
        2: 4,    # half a day
        3: 16,   # up to two days
        5: 24,   # few days (approx 3)
        8: 40,   # a week
        13: 80,  # full sprint (2 weeks)
        21: 120  # placeholder for 21+
    }
    stats_df['expected_hrs'] = stats_df['points'].map(benchmarks)

    # --- Plotting ---
    fig, ax1 = plt.subplots(figsize=(12, 7))

    # Actual Data
    ax1.plot(stats_df['points'], stats_df['turnaround_hrs'], 
             color='#2E86C1', marker='o', linewidth=3, markersize=8, label='Actual Avg Turnaround')
    
    # Expected Benchmark
    ax1.plot(stats_df['points'], stats_df['expected_hrs'], 
             color='#E67E22', linestyle='--', marker='s', alpha=0.8, label='Expected Benchmark')

    # Labels and Titles
    ax1.set_xlabel('Story Points', fontsize=12)
    ax1.set_ylabel('Time (Hours)', fontsize=12)
    plt.title('Actual vs. Expected Turnaround Time per Story Point', fontsize=16)
    
    # Legend and Grid
    plt.legend(loc='upper left')
    plt.grid(axis='y', linestyle=':', alpha=0.6)
    plt.xticks(stats_df['points'])

    # Annotate values
    for i, row in stats_df.iterrows():
        ax1.annotate(f"{row['turnaround_hrs']:.1f}h", 
                     (row['points'], row['turnaround_hrs']),
                     textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

    plt.tight_layout()
    plt.savefig("benchmark_comparison.png")
    print("Report generated: benchmark_comparison.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    process_tickets(args.file)
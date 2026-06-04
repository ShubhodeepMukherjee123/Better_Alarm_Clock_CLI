import argparse
import sys
import time
from datetime import datetime, timedelta

def validate_time_format(time_str):
    """
    Validates that the provided time string is in 'HH:MM' format
    and represents a valid 24-hour time.
    """
    try:
        # Check if the string matches the expected format by attempting to parse it
        parsed_time = datetime.strptime(time_str, "%H:%M")
        return parsed_time.hour, parsed_time.minute
    except ValueError:
        sys.stderr.write("Error: Invalid time format or out-of-bounds values. Please use 'HH:MM' (24-hour format).\n")
        sys.stderr.flush()  # Ensures the error streams out immediately
        sys.exit(1)

def get_target_datetime(target_hour, target_minute):
    """
    Calculates the target datetime for the alarm.
    If the target time has already passed today, schedules it for the next day.
    """
    now = datetime.now()
    target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    
    # Smart Chronological Scheduling: If the target time is in the past, add 1 day (24 hours)
    if target_time <= now:
        target_time += timedelta(days=1)
        
    return target_time

def run_alarm(target_datetime):
    """
    Runs the tracking loop and triggers the alarm when time is up.
    """
    try:
        # Phase 1: The Countdown Loop
        while True:
            now = datetime.now()
            if now >= target_datetime:
                break
                
            # Calculate remaining time
            remaining = target_datetime - now
            
            # Format remaining time as HH:MM:SS
            total_seconds = int(remaining.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            # Use carriage return (\r) to overwrite the line cleanly
            sys.stdout.write(f"\rTime remaining: {hours:02d}:{minutes:02d}:{seconds:02d}")
            sys.stdout.flush()
            
            # Sleep briefly to avoid high CPU usage while remaining highly responsive to Ctrl+C
            time.sleep(0.1)

    except KeyboardInterrupt:
        # Graceful exit explicitly for early cancellations
        print("\n\nAlarm cancelled by user before triggering. Exiting cleanly.")
        sys.exit(0)

    # Clear the countdown line fully before showing notifications
    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()

    # Zero-State Notification ASCII Art (High-End Production Blocks)
    ascii_art = """
 █     █  ███  █  █  █████     █   █  ████   █ 
 █     █ █   █ █ █   █         █   █  █   █  █ 
 █  █  █ █████ ██    ███       █   █  ████   █ 
 █ █ █ █ █   █ █ █   █         █   █  █      ▄ 
  █   █  █   █ █  █  █████      ███   █      █ 
    """
    # Print the large visual banner ONCE so it doesn't flood the terminal window
    sys.stdout.write(ascii_art)
    sys.stdout.write("\nPress Ctrl+C to silence the alarm and exit.\n")
    sys.stdout.flush()
    
    # Phase 2: Zero-State Notification Loop
    try:
        while True:
            sys.stdout.write("\a")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        # Graceful silence when the user shuts off an active alarm
        print("\nAlarm silenced. Clean shutdown complete. Goodbye!")
        sys.exit(0)

def main():
    # Setup argparse
    parser = argparse.ArgumentParser(description="Python CLI Alarm Clock")
    parser.add_argument(
        "time", 
        type=str, 
        help="Target alarm time in 24-hour HH:MM format (e.g., 14:30)"
    )
    
    args = parser.parse_args()
    
    # Validate and parse input
    target_hour, target_minute = validate_time_format(args.time)
    
    # Calculate target datetime
    target_datetime = get_target_datetime(target_hour, target_minute)
    
    print(f"Alarm successfully set for: {target_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    print("Tracking active... Close terminal or press Ctrl+C to cancel.")
    
    # Start the alarm runtime loop
    run_alarm(target_datetime)

if __name__ == "__main__":
    main()
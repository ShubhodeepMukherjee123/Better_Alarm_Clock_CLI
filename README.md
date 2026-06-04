# ⏰ Python CLI Alarm Clock

A robust, zero-dependency command-line alarm clock built in Python. This project was built with a focus on reliability, input validation, clean terminal UX, and cross-platform compatibility using only Python's standard library.

---

## 🚀 Features

### ✅ Strict Input Validation

* Accepts time only in valid 24-hour `HH:MM` format.
* Rejects invalid values such as `25:99` or `abc`.
* Displays clear error messages through `stderr`.

### ✅ Smart Scheduling

* Automatically detects if the requested alarm time has already passed today.
* Schedules the alarm for the next day when necessary.

### ✅ Live Countdown Timer

* Displays a real-time `HH:MM:SS` countdown.
* Uses carriage returns (`\r`) to update the same terminal line.
* Prevents terminal flooding and excessive scrolling.

### ✅ Zero-Dependency Alarm

* Uses the native ASCII bell character (`\a`) for notifications.
* Displays a large visual "WAKE UP!" banner when the alarm triggers.
* No external packages or audio libraries required.

### ✅ Graceful Shutdown

* Handles `Ctrl + C` (`KeyboardInterrupt`) cleanly.
* Separate handling for:

  * Cancelling before the alarm triggers.
  * Silencing an active alarm.

---

## 🛠️ Requirements

* Python 3.6+

No external dependencies are required.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/ShubhodeepMukherjee123/Better_Alarm_Clock_CLI.git
cd Better_Alarm_Clock_CLI
```

---

## ▶️ Usage

Display help:

```bash
python alarm.py -h
```

Set an alarm:

```bash
python alarm.py 14:30
```

Example output:

```text
Alarm successfully set for: 2026-06-05 14:30:00
Tracking active... Close terminal or press Ctrl+C to cancel.

Time remaining: 00:15:42
```

---

## 🔔 Alarm Trigger

When the countdown reaches zero:

* The terminal displays a large visual banner.
* The system bell (`\a`) sounds every second.
* The alarm continues until the user presses `Ctrl + C`.

Example:

```text
 █     █  ███  █  █  █████     █   █  ████   █
 █     █ █   █ █ █   █         █   █  █   █  █
 █  █  █ █████ ██    ███       █   █  ████   █
 █ █ █ █ █   █ █ █   █         █   █  █      ▄
  █   █  █   █ █  █  █████      ███   █      █

Press Ctrl+C to silence the alarm and exit.
```

---

## 🏗️ Design Decisions

### Argparse for CLI Input

The application uses `argparse` to provide a standard command-line interface and built-in help documentation.

### Smart Next-Day Scheduling

If the requested time has already passed for the current day, the alarm is automatically scheduled for the following day.

### Single-Threaded Architecture

A simple synchronous loop was chosen over threads or async frameworks because the application only manages a single alarm.

Benefits:

* Easier to reason about
* No race conditions
* Minimal complexity
* Perfectly adequate for the assignment scope

### Clean Terminal Rendering

The countdown updates on a single line using:

```python
sys.stdout.write("\r")
```

This avoids flooding the terminal with new output.

### Zero External Dependencies

Everything is implemented using Python's standard library, making the application easy to run on Windows, macOS, and Linux.

---

## 🧪 Edge Cases Handled

| Scenario          | Example                                         | Behavior                 |
| ----------------- | ----------------------------------------------- | ------------------------ |
| Invalid format    | `python alarm.py abc`                           | Displays error and exits |
| Invalid time      | `python alarm.py 25:99`                         | Displays error and exits |
| Past time         | `python alarm.py 09:00` when it's already 10:00 | Schedules for tomorrow   |
| User cancellation | `Ctrl + C` during countdown                     | Exits cleanly            |
| Alarm silencing   | `Ctrl + C` during alarm                         | Stops alarm and exits    |

---

## 📁 Project Structure

```text
cli-alarm-clock/
│
├── alarm.py
├── README.md
└── LICENSE
```

---

## 🎯 Assignment Scope

This project intentionally focuses on a well-defined MVP:

Included:

* Input validation
* Smart scheduling
* Live countdown
* Alarm notifications
* Signal handling

Not Included:

* Multiple alarms
* Background daemon support
* Alarm persistence
* GUI interface
* External audio libraries

The goal was to build a reliable, maintainable solution within the constraints of a short engineering exercise.

---

## 📄 License

This project is licensed under the MIT License.

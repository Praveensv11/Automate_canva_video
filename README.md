# Automatic Video Creator

This Python script automates the creation of videos by utilizing the PyAutoGUI library. It simulates mouse and keyboard inputs to interact with video editing software and generate workout videos.

## Compatibility

Please note that this script may not work on all systems due to variations in screen resolution and layout. It has been tested and confirmed to work on the author's system, but adjustments may be necessary for use on different setups.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- PyAutoGUI library (`pip install pyautogui`)
- Video editing software (e.g., Adobe Premiere Pro, Final Cut Pro, etc.)

## Usage

1. Clone this repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Open your preferred video editing software and load the project/template where you want to generate the workout video.
4. Adjust the script according to your requirements. Ensure that mouse and keyboard coordinates match the layout of your editing software.
5. Run the script using `python workout_video_creator.py`.
6. Follow any on-screen instructions provided by the script.

## Notes

- This script relies heavily on PyAutoGUI to simulate user inputs. It may not work as expected if the layout of the editing software changes or if there are significant differences in screen resolution.
- Be cautious when running the script, as it will simulate mouse and keyboard inputs. Ensure that the video editing software is in focus and that there are no obstructions on the screen during execution.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

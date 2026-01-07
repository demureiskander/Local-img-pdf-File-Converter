# ImageFlow

ImageFlow is a lightweight offline desktop application for converting images between different formats and exporting them into a single PDF file.

The application works fully locally on your machine — no internet connection, no cloud uploads, and no data tracking.

---

## Key Features

- Convert images between popular formats:
  - JPG / JPEG
  - PNG
  - WEBP
- Export multiple images into a single PDF
- Batch image processing
- Drag & Drop support
- Offline usage (privacy-friendly)
- Clean and minimal desktop UI
- Native Windows executable (.exe)

---

## Supported Platforms

- Windows 10 / 11

---

## Built With

- Python 3
- CustomTkinter — modern desktop UI
- Pillow — image processing
- PyInstaller — Windows executable packaging

---

## Project Structure

```
ImageConverter/
├── app.py              # Main application UI
├── converter.py        # Image conversion logic
├── imageflow.spec      # PyInstaller build configuration
├── requirements.txt    # Python dependencies
├── icon.ico            # Application icon
```

---

## Running the Application (Development)

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the application:

```
python app.py
```

---

## Building the Windows Executable

To build the Windows `.exe` file:

```
python -m PyInstaller imageflow.spec
```

The final executable will be located at:

```
dist/ImageFlow/ImageFlow.exe
```

---

## Motivation

ImageFlow was created as a simple, fast, and private alternative to online image conversion services.

The goal was to build a tool that:
- works offline
- keeps user files local
- provides a clean and focused user experience
- avoids unnecessary complexity

---

## Roadmap (Optional Ideas)

- One-file executable build
- Folder-based batch conversion
- Presets for web / print / PDF export
- Light / dark theme toggle
- Automatic opening of output folder after conversion

---

## License

This project is licensed under the MIT License.

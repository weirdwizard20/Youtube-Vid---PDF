# YouTube Video to PDF Converter

The YouTube Video to PDF Converter is a Python script that allows users to convert YouTube videos into PDF documents containing frames extracted from the video at regular intervals.

## Introduction

This script utilizes the `pytube`, `yt_dlp`, `opencv-python`, `Pillow`, and `fpdf` libraries to download YouTube videos, extract frames from the videos, and generate a PDF document containing the extracted frames along with timestamps and `flask` to deploy it as a website.

## Features

- Downloads YouTube videos using either `pytube` or `yt_dlp`.
- Extracts frames from the downloaded videos at regular intervals.
- Converts the extracted frames into a PDF document.
- Adds timestamps to each frame in the PDF document.

# AcrylicEdgeDetection
This repository contains an edge-detection script for laser cutting musical album covers

I wrote this script to help with the image processing of a mini art project my friends and I wished to create. The idea was to engrave our favorite musical artists'
album covers onto an 18 by 12 inch sheet of acrylic using a laser cutter. The images of the album covers were all saved from the spotify app, so they each
included a spotify song code on the bottom. Each cover also had to be converted to a highly contrasted, black or white image with sharp lines and crevices since the laser itself can only cut or skip designated areas on the acrylic sheet (it cannot dynamically adjust its power level to account for grayscale data). I decided to create this  python script in order to streamline the processing of each image. It runs every album cover through a grayscale filter, edge detection, inversion (switching blacks with whites and vice versa), and a contrast boost. 

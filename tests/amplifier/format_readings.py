#!/usr/bin/python
import math

# sine 60Hz
#readings = [0, 0, 0, 2, 6, 14, 22, 30, 39, 46, 47, 48, 45, 40, 30, 19, 11, 6, 2, 0, 2, 6, 15, 26, 39, 48, 55, 58, 58, 50, 40, 28, 17, 12, 5, 0, 2, 3, 9, 18, 26, 36, 44, 49, 51, 48, 44, 35, 24, 14, 6, 2, 1, 1, 6, 13, 25, 37, 43, 50, 55, 55, 50, 45, 38, 27, 15, 6, 2, 1, 2, 5, 13, 25, 35, 44, 49, 52, 50, 44, 35, 27, 17, 8, 3, 1, 1, 3, 9, 22, 29, 39, 49, 55, 57, 58, 51, 38, 27, 15, 6, 3, 1, 1, 5, 13, 22, 30, 39, 49, 50, 48, 45, 38, 26, 18, 9, 4, 2, 0, 1, 8, 14, 25, 38, 49, 56, 59, 56, 49, 41, 29, 16, 10, 4, 1, 1, 4, 10, 20, 26, 35, 43, 48, 49, 46, 44, 35, 25, 16, 7, 2, 0, 0, 4, 12, 26, 37, 49, 50, 54, 58, 51, 42, 30, 23, 13, 6, 2, 0, 2, 7, 12, 24, 35, 43, 49, 51, 51, 46, 37, 28, 18, 9, 3, 1, 0, 3, 9, 21, 31, 42, 49, 55, 56, 53, 45, 42, 29, 18, 8, 2, 1, 0, 5, 13, 22, 32, 41, 47, 50, 51, 45, 37, 29, 20, 12, 3, 2, 1, 2, 7, 15, 26, 38, 47, 54, 58, 57, 51, 41, 31, 20, 9, 5, 1, 2, 3, 10, 17, 27, 36, 43, 47, 48, 46, 40, 31, 21, 12, 6, 2, 1, 0, 6, 12, 23, 34, 47, 55, 60, 57, 51, 43, 32, 22, 14, 6, 2, 1, 3, 6, 14, 23, 33, 42, 47, 50, 49, 46, 38, 29, 17, 8, 3, 1, 1, 3, 10, 21, 30, 41, 53, 54, 57, 55, 47, 34, 26, 16, 8, 2, 1, 1, 4, 11, 20, 32, 41, 47, 50, 49, 45, 37, 31, 21, 11, 5, 2, 1, 1, 6, 14, 28, 40, 46, 54, 56, 56, 49, 43, 32, 18, 8, 2, 2, 0, 3, 10, 20, 30, 36, 43, 49, 49, 46, 41, 33, 23, 13, 5, 3, 0, 3, 4, 13, 23, 33, 46, 54, 58, 60, 53, 46, 33, 21, 12, 5, 2, 0, 3, 9, 16, 25, 36, 42, 45, 48, 47, 42, 34, 28, 18, 11, 4, 0, 1, 3, 10, 20, 34, 45, 51, 59, 58, 54, 45, 35, 24, 14, 6, 2, 1, 1, 6, 9, 21, 31, 39, 46, 48, 48, 47, 40, 29, 22, 12, 5, 1, 0, 2, 7, 19, 27, 38, 47, 52, 55, 55, 48, 39, 28, 17, 11, 4, 2, 1, 2, 10, 18, 29, 39, 47, 51, 50, 47, 41, 32, 21, 13, 5, 2, 0, 3, 4, 13, 23, 34, 45, 53, 58, 58, 53, 44, 35, 24, 13, 4, 2, 0, 2, 8, 17, 28, 34, 41, 45, 48, 46, 42, 35, 25, 15, 8, 3, 1, 1, 2, 8, 19, 30, 43, 52, 59, 58, 55, 45, 37, 24, 16, 7, 3, 1, 2, 7, 15, 19, 30, 39, 45, 50, 49, 46, 39, 30, 21, 11, 5, 1, 0, 2, 8, 17, 25, 36, 46, 56, 56, 55, 49, 37, 27, 17, 13, 4, 4, 1, 4, 8, 17, 28, 38, 46, 51, 52, 48, 41, 32, 22, 14, 6, 4, 1, 3, 6, 11, 21, 33, 45, 52, 57, 55, 51, 47, 37, 23, 12, 4, 2, 0, 1, 7, 15, 25, 37, 45, 44, 47, 47, 42, 33, 27, 17, 9, 3, 1, 0, 2, 10, 20, 30, 41, 52, 58, 61, 56, 49, 37, 26, 16, 6, 2, 2, 1, 5, 15, 22, 29, 39, 45, 49, 47, 44, 36, 33, 22, 11, 5, 2, 0, 1, 7, 17, 27, 39, 49, 57, 57, 55, 49, 39, 28, 17, 9, 3, 1, 1, 3, 9, 18, 27, 37, 45, 50, 51, 49, 43, 33, 24, 13, 6, 3, 0, 1, 6, 12, 23, 35, 43, 51, 54, 56, 51, 42, 33, 25, 14, 6, 3, 0, 1, 7, 15, 25, 34, 46, 50, 46, 48, 43, 35, 25, 15, 9, 3, 1, 0, 3, 8, 18, 29, 41, 50, 57, 59, 54, 49, 38, 27, 16, 7, 2, 0, 1, 6, 15, 23, 30, 38, 45, 48, 46, 44, 35, 30, 23, 13, 7, 2, 0, 1, 6, 16, 28, 40, 50, 57, 60, 56, 51, 41, 29, 19, 11, 1, 2, 2, 2, 8, 16, 29, 35, 44, 48, 50, 49, 43, 34, 22, 13, 6, 3, 0, 0, 5, 12, 24, 37, 43, 51, 55, 55, 52, 45, 30, 20, 13, 5, 2, 1, 3, 6, 15, 25, 34, 43, 50, 52, 48, 44, 36, 27, 15, 10, 4, 2, 1, 5, 10, 16, 31, 41, 50, 55, 58, 58, 51, 40, 27, 15, 7, 2, 1, 1, 5, 13, 22, 32, 44, 47, 48, 49, 44, 37, 27, 18, 10, 4, 2, 0, 2, 8, 14, 26, 38, 49, 56, 59, 56, 50, 40, 31, 20, 10, 3, 1, 1, 3, 13, 18, 28, 37, 43, 48, 49, 45, 41, 36, 26, 15, 6, 2, 0, 0, 5, 13, 22, 37, 48, 53, 56, 57, 51, 42, 32, 22, 13, 5, 2, 1, 1, 6, 12, 24, 33, 42, 49, 52, 50, 45, 36, 27, 17, 8, 2, 1, 1, 4, 11, 19, 29, 41, 48, 52, 55, 53, 47, 37, 25, 15, 7, 3, 1, 1, 3, 12, 23, 32, 41, 49, 49, 50, 46, 38, 30, 20, 11, 3, 2, 1, 2, 6, 15, 25, 37, 48, 55, 58, 57, 51, 42, 30, 20, 10, 4, 1, 1, 4, 11, 17, 26, 39, 45, 48, 47, 45, 38, 30, 25, 13, 6, 3, 1, 1, 4, 13, 23, 36, 46, 55, 56, 57, 53, 43, 32, 23, 13, 5, 0, 0, 1, 7, 16, 24, 33, 41, 47, 50, 50, 46, 37, 27, 18, 9, 3, 1, 0, 3, 10, 20, 36, 39, 48, 56, 54, 50, 44, 35, 24, 16]

# sine 30Hz
#readings = [0, 0, 0, 0, 1, 4, 4, 9, 15, 18, 23, 28, 35, 40, 47, 51, 54, 57, 58, 58, 58, 56, 50, 50, 47, 41, 37, 31, 24, 19, 12, 9, 5, 2, 1, 0, 0, 0, 2, 4, 7, 12, 16, 23, 32, 38, 46, 46, 54, 58, 62, 64, 67, 67, 66, 65, 61, 55, 49, 42, 35, 27, 21, 14, 10, 7, 3, 1, 0, 0, 0, 0, 2, 6, 10, 15, 21, 27, 32, 36, 40, 46, 50, 55, 58, 59, 59, 58, 57, 54, 48, 42, 37, 31, 28, 22, 16, 13, 8, 3, 1, 0, 0, 0, 0, 2, 5, 8, 15, 20, 27, 31, 38, 45, 51, 58, 63, 66, 68, 66, 65, 64, 61, 58, 53, 43, 38, 35, 28, 20, 14, 9, 6, 3, 0, 0, 0, 0, 1, 3, 6, 12, 17, 21, 27, 33, 39, 45, 50, 51, 53, 57, 57, 56, 55, 56, 54, 49, 44, 37, 31, 25, 20, 15, 10, 6, 3, 1, 0, 0, 0, 0, 2, 7, 10, 15, 21, 29, 36, 43, 49, 50, 56, 61, 66, 67, 68, 68, 66, 62, 56, 50, 43, 37, 29, 23, 17, 14, 8, 4, 2, 0, 0, 0, 0, 1, 5, 9, 14, 18, 24, 30, 35, 38, 45, 49, 55, 57, 59, 60, 58, 57, 53, 48, 45, 38, 34, 29, 23, 19, 14, 8, 6, 2, 0, 0, 0, 0, 2, 4, 9, 10, 17, 23, 29, 36, 44, 51, 57, 60, 64, 68, 65, 65, 63, 62, 58, 54, 49, 43, 37, 29, 23, 17, 9, 5, 4, 1, 0, 0, 0, 0, 3, 4, 9, 14, 19, 26, 31, 39, 45, 48, 48, 51, 57, 57, 58, 59, 58, 54, 51, 46, 39, 33, 27, 22, 17, 11, 8, 4, 1, 1, 0, 0, 0, 2, 4, 8, 14, 19, 25, 35, 41, 47, 50, 55, 60, 62, 67, 69, 69, 65, 60, 55, 51, 47, 40, 34, 25, 18, 15, 9, 6, 3, 1, 0, 0, 0, 1, 4, 8, 11, 15, 20, 25, 34, 38, 43, 49, 53, 56, 59, 60, 56, 55, 53, 49, 49, 43, 39, 31, 24, 21, 17, 12, 6, 2, 1, 0, 0, 0, 1, 3, 7, 9, 14, 20, 27, 35, 43, 49, 56, 60, 60, 62, 64, 64, 63, 63, 60, 55, 53, 46, 39, 32, 25, 19, 13, 7, 3, 1, 0, 0, 0, 1, 1, 4, 7, 13, 18, 24, 30, 36, 41, 45, 48, 53, 56, 55, 58, 59, 59, 54, 52, 45, 40, 34, 28, 23, 17, 12, 9, 5, 2, 1, 0, 0, 0, 1, 4, 7, 13, 18, 24, 30, 37, 42, 49, 54, 61, 64, 67, 69, 68, 66, 62, 57, 51, 48, 43, 35, 31, 24, 17, 12, 6, 3, 1, 0, 0, 0, 1, 3, 7, 8, 14, 19, 25, 30, 37, 43, 48, 53, 54, 55, 55, 56, 56, 53, 50, 49, 45, 40, 34, 28, 22, 17, 13, 7, 3, 1, 0, 0, 0, 0, 2, 4, 7, 13, 18, 26, 33, 40, 48, 55, 59, 58, 61, 65, 66, 67, 67, 63, 61, 54, 48, 40, 34, 27, 20, 13, 9, 5, 2, 0, 0, 0, 0, 1, 3, 6, 11, 17, 21, 27, 34, 39, 44, 48, 51, 55, 58, 58, 60, 60, 56, 51, 46, 41, 35, 30, 25, 21, 15, 9, 7, 3, 1, 0, 0, 0, 1, 3, 7, 12, 14, 20, 25, 33, 39, 47, 54, 60, 63, 67, 69, 65, 64, 62, 57, 52, 51, 43, 36, 30, 26, 18, 12, 7, 3, 2, 1, 0, 0, 0, 2, 6, 7, 11, 18, 23, 29, 36, 41, 47, 50, 53, 55, 57, 57, 57, 57, 53, 52, 49, 43, 36, 29, 24, 18, 13, 8, 5, 2, 0, 0, 0, 0, 2, 3, 6, 11, 17, 23, 33, 38, 44, 50, 54, 58, 63, 66, 68, 67, 66, 64, 59, 54, 48, 41, 35, 27, 23, 18, 9, 7, 5, 0, 0, 0, 0, 0, 2, 6, 10, 15, 20, 25, 33, 34, 42, 47, 49, 56, 58, 60, 59, 58, 54, 51, 46, 42, 36, 33, 27, 22, 17, 11, 8, 2, 1, 1, 0, 0, 0, 3, 6, 10, 16, 19, 24, 31, 39, 46, 53, 59, 65, 68, 65, 65, 64, 62, 59, 56, 53, 48, 42, 36, 28, 20, 15, 10, 5, 2, 0, 0, 0, 0, 2, 3, 7, 10, 15, 21, 28, 36, 36, 42, 46, 50, 53, 57, 59, 58, 56, 54, 51, 50, 44, 37, 31, 25, 20, 15, 10, 6, 3, 1, 0, 0, 0, 1, 3, 5, 10, 16, 23, 29, 36, 43, 48, 52, 57, 62, 66, 70, 69, 68, 65, 61, 54, 48, 43, 35, 32, 26, 19, 13, 6, 4, 2, 0, 0, 0, 0, 2, 5, 9, 14, 19, 21, 27, 33, 39, 45, 51, 55, 58, 56, 60, 59, 54, 52, 48, 42, 39, 36, 29, 25, 19, 13, 9, 5, 2, 1, 0, 0, 0, 2, 4, 8, 12, 18, 22, 29, 38, 44, 50, 56, 60, 63, 64, 65, 66, 65, 63, 59, 54, 51, 43, 36, 30, 24, 18, 11, 4, 3, 2, 0, 0, 0, 1, 3, 5, 9, 14, 20, 26, 33, 37, 45, 45, 51, 53, 56, 59, 60, 59, 57, 54, 49, 44, 39, 32, 26, 21, 15, 11, 8, 4, 1, 1, 0, 0, 0, 2, 5, 9, 14, 21, 28, 32, 38, 44, 51, 56, 61, 65, 67, 71, 69, 65, 60, 56, 49, 46, 40, 34, 26, 22, 16, 10, 5, 2, 0, 0, 0, 0, 2, 4, 7, 11, 15, 19, 27, 33, 39, 45, 49, 51, 58, 58, 59, 58, 55, 53, 50, 45, 44, 38, 33, 27, 20, 13, 8, 6, 2, 1, 0, 0, 0, 1, 4, 7, 9, 14, 20, 27, 35, 43, 50, 58, 57, 60, 63, 65, 68, 67, 66, 62, 58, 51, 45, 38, 31, 24, 16, 13, 5, 4]

# sine 10Hz
readings = [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 3, 0, 5, 6, 7, 8, 10, 10, 13, 14, 15, 17, 19, 22, 25, 27, 29, 29, 34, 32, 35, 37, 40, 43, 45, 47, 48, 51, 50, 51, 52, 55, 57, 58, 60, 60, 63, 59, 61, 60, 58, 61, 62, 61, 64, 63, 62, 60, 58, 56, 56, 56, 55, 55, 55, 52, 52, 48, 44, 43, 41, 38, 38, 36, 36, 33, 31, 29, 26, 23, 20, 19, 17, 15, 14, 13, 10, 10, 10, 7, 5, 4, 3, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 4, 5, 7, 8, 10, 11, 13, 15, 17, 18, 19, 23, 27, 29, 33, 33, 37, 37, 38, 43, 43, 47, 50, 53, 57, 56, 57, 58, 62, 62, 63, 66, 69, 70, 69, 72, 68, 73, 71, 70, 69, 71, 73, 72, 71, 70, 69, 68, 63, 62, 61, 60, 61, 58, 57, 58, 53, 49, 46, 44, 42, 40, 38, 36, 36, 34, 31, 28, 26, 21, 18, 16, 14, 14, 13, 8, 8, 8, 4, 6, 3, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 4, 4, 5, 6, 7, 9, 12, 13, 13, 16, 18, 18, 20, 22, 25, 29, 31, 34, 34, 36, 37, 39, 40, 43, 45, 49, 50, 52, 53, 54, 54, 54, 57, 58, 60, 61, 63, 64, 62, 62, 61, 59, 60, 62, 62, 63, 62, 61, 60, 57, 55, 53, 52, 52, 51, 47, 50, 47, 46, 41, 40, 37, 36, 33, 32, 28, 29, 26, 24, 24, 20, 17, 15, 14, 13, 12, 8, 7, 7, 5, 4, 4, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 5, 6, 7, 9, 10, 13, 15, 18, 18, 20, 24, 24, 27, 32, 34, 37, 40, 44, 43, 43, 45, 49, 52, 54, 56, 59, 62, 64, 65, 63, 65, 65, 69, 70, 72, 70, 72, 73, 71, 72, 69, 67, 69, 70, 70, 70, 68, 67, 66, 64, 62, 57, 57, 56, 58, 55, 52, 51, 47, 44, 42, 38, 34, 32, 33, 31, 28, 26, 22, 19, 17, 15, 13, 11, 11, 11, 9, 7, 5, 3, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 3, 5, 5, 6, 8, 9, 10, 12, 14, 17, 18, 20, 22, 22, 24, 26, 30, 31, 36, 37, 39, 42, 42, 43, 45, 47, 49, 51, 52, 56, 57, 58, 57, 57, 58, 60, 59, 61, 63, 63, 62, 63, 61, 64, 61, 59, 58, 59, 59, 58, 58, 56, 53, 52, 49, 45, 46, 46, 45, 44, 41, 40, 36, 34, 31, 29, 26, 25, 24, 23, 21, 19, 17, 14, 12, 10, 8, 6, 5, 4, 5, 4, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 4, 7, 7, 9, 9, 10, 12, 13, 17, 19, 22, 23, 25, 28, 30, 33, 36, 36, 42, 44, 48, 50, 52, 53, 53, 55, 57, 59, 63, 66, 67, 69, 66, 66, 67, 67, 72, 70, 72, 70, 72, 74, 71, 71, 69, 67, 66, 66, 66, 67, 65, 64, 58, 56, 55, 54, 50, 50, 49, 47, 43, 42, 40, 37, 35, 31, 28, 25, 25, 22, 20, 18, 15, 14, 12, 11, 8, 6, 6, 5, 3, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 3, 7, 7, 9, 8, 11, 12, 13, 15, 17, 21, 22, 25, 27, 32, 28, 30, 33, 37, 39, 40, 43, 45, 47, 48, 49, 49, 51, 54, 55, 56, 59, 60, 61, 57, 57, 60, 60, 62, 63, 63, 63, 63, 62, 61, 59, 58, 57, 55, 58, 57, 55, 54, 50, 49, 47, 43, 41, 42, 39, 38, 36, 35, 33, 29, 28, 25, 23, 20, 19, 18, 16, 16, 14, 12, 10, 8, 6, 5, 4, 2, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 3, 4, 4, 8, 9, 10, 11, 11, 13, 16, 17, 20, 24, 27, 31, 34, 33, 35, 38, 42, 42, 45, 49, 49, 53, 57, 58, 59, 60, 60, 62, 64, 66, 69, 72, 72, 68, 68, 66, 69, 71, 72, 72, 73, 72, 70, 70, 68, 66, 64, 63, 62, 61, 61, 60, 59, 56, 51, 51, 46, 43, 44, 43, 40, 36, 34, 33, 30, 27, 23, 21, 18, 17, 16, 14, 12, 10, 8, 6, 4, 4, 3, 3, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 3, 3, 7, 6, 8, 9, 11, 13, 15, 15, 17, 18, 21, 23, 27, 29, 32, 33, 33, 35, 37, 39, 41, 45, 48, 49, 50, 48, 52, 52, 53, 55, 57, 59, 60, 64, 62, 61, 62, 60, 60, 61, 63, 62, 61, 62, 62, 60, 58, 56, 55, 54, 53, 50, 52, 51, 49, 46, 43, 42, 38, 36, 37, 34, 32, 30, 28, 26, 24, 22, 20, 17, 15, 14, 12, 12, 10, 8, 7, 7, 2, 4, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3, 5, 7, 7, 10, 12, 14, 16, 18, 18, 20, 22, 24, 27, 31, 34, 38, 39, 43, 43, 44, 45, 48, 53, 55, 58, 60, 62, 61, 61, 63, 65, 67, 69, 70, 72, 75, 70, 70, 68, 69, 71, 71, 72, 71, 70, 68, 66, 65, 63, 60, 60, 60, 61, 58, 54, 52, 51, 48, 48, 44, 41, 36, 35, 33, 31, 31, 28, 25, 22, 19, 17, 14, 13, 13, 11, 9, 8, 6, 8, 4, 2, 2, 1, 0, 0, 0]

total_millis = 500.0
nsamples = len(readings)

for i in range(nsamples):
    m = i*total_millis/nsamples

    # 60 Hz => 1/60 = .01(6) seconds per period
    # m * 60/1000 goes from 0 to 1 in .01(6) seconds
    # m * 60/1000 * 2 * pi goes from 0 to 2 pi 60 times per second

# sine 60Hz
#    print ("%.1f, %.3f, %.3f"% (m, .7*math.sin(m*60*2*math.pi/1000), readings[i]))
# sine 30Hz
#    print ("%.1f, %.3f, %.3f"% (m, .7*math.sin(m*30*2*math.pi/1000), readings[i]))
# sine 10Hz
    print ("%.1f, %.3f, %.3f"% (m, .7*math.sin(m*10*2*math.pi/1000), readings[i]))

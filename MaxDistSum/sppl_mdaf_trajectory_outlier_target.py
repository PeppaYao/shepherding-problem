import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
xx = np.array([54.810, 54.636, 54.445, 54.241, 54.056, 53.869, 53.685, 53.473, 53.258, 53.038, 52.820, 52.581, 52.364, 52.158, 51.959, 51.733, 51.501, 51.292, 51.078, 50.865, 50.654, 50.419, 50.191, 49.941, 49.709, 49.482, 49.260, 49.008, 48.776, 48.555, 48.349, 48.099, 47.834, 47.600, 47.342, 47.090, 46.830, 46.595, 46.374, 46.159, 45.960, 45.767, 45.576, 45.399, 45.233, 45.021, 44.797, 44.574, 44.352, 44.122, 43.871, 43.593, 43.359, 43.073, 42.832, 42.635, 42.470, 42.338, 42.239, 42.165, 42.123, 42.112, 42.130, 42.163, 42.225, 42.321, 42.446, 42.613, 42.810, 43.038, 43.299, 43.594, 43.925, 44.286, 44.684, 45.121, 45.589, 46.097, 46.642, 47.224, 47.848, 48.505, 49.205, 49.939, 50.710, 51.497, 52.351, 53.246, 54.184, 55.165, 56.189, 57.233, 58.324, 59.463, 60.649, 61.887, 63.170, 64.501, 65.882, 67.311, 68.798, 70.336, 71.926, 73.727, 75.530, 77.334, 79.139, 80.944, 82.751, 84.558, 86.369, 88.178, 89.990, 91.802, 93.616, 95.432, 97.248, 99.068, 100.887, 102.710, 104.533, 106.359, 108.187, 110.017, 111.846, 113.677, 115.508, 117.342, 119.176, 121.013, 122.851, 124.690, 126.532, 128.374, 130.218, 132.065, 133.913, 135.765, 137.619, 139.476, 141.335, 143.195, 145.057, 146.920, 148.785, 150.650, 152.518, 154.387, 156.257, 158.131, 160.007, 161.886, 163.765, 165.648, 167.535, 169.423, 171.314, 173.206, 175.099, 176.995, 178.891, 180.793, 182.694, 184.599, 186.504, 188.410, 190.317, 192.228, 194.140, 196.056, 197.973, 199.891, 201.814, 203.739, 205.667, 207.598, 209.529, 211.465, 213.401, 215.340, 217.279, 219.224, 221.170, 223.118, 225.069, 227.021, 228.975, 230.933, 232.891, 234.852, 236.816, 238.782, 240.750, 242.721, 244.695, 246.669, 248.644, 250.621, 252.601, 254.585, 256.571, 258.558, 260.546, 262.537, 264.529, 266.523, 268.518, 270.515, 272.513, 274.511, 276.511, 278.511, 280.511, 282.511, 284.510, 286.509, 288.506, 290.502, 292.497, 294.488, 296.476, 298.463, 300.445, 302.424, 304.396, 306.365, 308.330, 310.285, 312.234, 314.176, 316.113, 318.032, 319.944, 321.847, 323.745, 325.618, 327.490, 329.346, 331.207, 333.044, 334.877, 336.648, 338.376, 340.082, 341.718, 343.330, 344.898, 346.437, 347.802, 349.098, 350.230, 351.208, 351.973, 352.645, 353.482, 351.576, 353.503, 353.458, 355.454, 354.014, 354.688, 353.192, 354.635, 355.510, 357.510, 355.774, 357.499, 355.984, 357.981, 359.519, 357.557, 359.538, 359.247, 360.467, 359.648, 360.256, 360.474, 362.055, 361.377, 361.524, 361.837, 361.873, 362.926, 363.269, 363.757, 363.998, 364.711, 363.419, 365.349, 366.383, 364.544, 365.986, 366.672, 368.480, 366.533, 368.478, 369.143, 369.932, 368.920, 369.987, 370.739, 372.567, 370.569, 372.043, 373.109, 371.474, 372.857, 373.739, 374.581, 375.980, 373.982, 375.758, 376.738, 378.682, 376.683, 378.008, 379.208, 377.271, 378.976, 378.498, 379.737, 378.935, 380.333, 378.587, 380.578, 380.194, 381.022, 379.776, 381.663, 380.903, 382.786, 381.620, 383.561, 381.931, 383.931, 384.625, 386.624, 384.940, 386.419, 385.369, 387.223, 388.179, 389.692, 388.832, 389.788, 388.027, 389.974, 389.808, 390.416, 390.223, 390.829, 391.409, 392.272, 391.205, 391.965, 392.525, 393.397, 393.140, 393.602, 394.653, 392.737, 394.417, 395.083, 396.798, 394.813, 396.068, 395.987, 397.490, 396.861, 397.082, 398.924, 397.865, 398.972, 397.106, 399.072, 397.944, 399.856, 399.258, 401.231, 400.579, 402.572, 400.772, 402.561, 402.937, 401.021, 402.829, 403.686, 404.707, 402.713, 404.569, 405.790, 404.729, 406.593, 405.163, 406.837, 406.410, 408.183, 407.172, 409.113, 408.136, 409.942, 409.747, 411.298, 409.323, 410.965, 411.122, 411.900, 411.547, 411.913, 410.699, 411.591, 412.423, 412.651, 414.337, 413.083, 413.445, 411.763, 412.862, 413.625, 413.299, 413.814, 414.402, 414.324, 414.700, 415.056, 416.073, 415.563, 416.655, 415.892, 416.674, 417.962, 419.849, 417.937, 419.903, 418.254, 420.213, 421.091, 421.321, 421.371, 421.131, 423.021, 422.447, 424.393, 423.250, 425.244, 424.151, 424.847, 423.329, 424.822, 425.313, 426.180, 425.066, 425.954, 427.247, 426.787, 428.631, 427.794, 428.879, 430.020, 428.052, 429.525, 430.546, 430.478, 431.411, 431.015, 432.664, 430.792, 432.075, 430.537, 432.521, 432.736, 433.663, 431.939, 433.289, 434.450, 434.955, 436.651, 434.853, 436.624, 436.563, 437.917, 436.562, 437.368, 438.250, 439.697, 437.734, 439.698, 441.343, 441.829, 443.529, 442.784, 444.429, 445.224, 444.147, 445.307, 446.151, 446.354, 446.698, 446.856, 446.721, 447.532, 447.005, 448.830, 447.660, 448.585, 447.864, 449.807, 449.662, 451.635, 449.798, 450.927, 451.681, 453.464, 451.527, 453.349, 453.739, 455.739, 453.874, 454.583, 455.503, 454.821, 455.417, 455.702, 456.486, 455.286, 457.249, 456.569, 458.404, 457.132, 459.057, 459.084, 457.628, 459.528, 459.008, 460.861, 459.554, 460.921, 459.241, 461.140, 461.314, 462.823, 462.175, 462.412, 464.411, 463.365, 465.338, 463.962, 464.465, 466.254, 464.748, 466.651, 465.746, 467.740, 466.509, 468.390, 470.069, 468.193, 470.139, 471.912, 470.700, 472.694, 473.178, 471.187, 472.661, 473.566, 475.407, 473.631, 475.536, 474.596, 476.517, 476.684, 478.055, 476.090, 477.930, 478.904, 478.931, 480.006, ])
yy = np.array([551.005, 547.008, 543.013, 539.018, 535.022, 531.027, 527.031, 523.037, 519.042, 515.048, 511.054, 507.062, 503.067, 499.073, 495.078, 491.084, 487.091, 483.096, 479.102, 475.108, 471.113, 467.120, 463.127, 459.134, 455.141, 451.148, 447.154, 443.162, 439.168, 435.175, 431.180, 427.188, 423.197, 419.203, 415.212, 411.220, 407.228, 403.235, 399.241, 395.247, 391.252, 387.257, 383.261, 379.265, 375.268, 371.274, 367.280, 363.287, 359.293, 355.299, 351.307, 347.317, 343.324, 339.334, 335.341, 331.346, 327.349, 323.352, 319.353, 315.354, 311.354, 307.354, 303.354, 299.354, 295.354, 291.356, 287.358, 283.361, 279.366, 275.372, 271.381, 267.392, 263.406, 259.422, 255.442, 251.466, 247.493, 243.526, 239.563, 235.605, 231.654, 227.709, 223.770, 219.838, 215.913, 211.992, 208.084, 204.185, 200.297, 196.419, 192.552, 188.691, 184.842, 181.008, 177.188, 173.384, 169.596, 165.824, 162.070, 158.333, 154.620, 150.928, 147.257, 146.389, 145.523, 144.659, 143.799, 142.937, 142.079, 141.223, 140.373, 139.521, 138.673, 137.827, 136.986, 136.146, 135.310, 134.479, 133.650, 132.825, 132.004, 131.189, 130.376, 129.569, 128.760, 127.955, 127.150, 126.352, 125.554, 124.764, 123.975, 123.191, 122.411, 121.631, 120.858, 120.090, 119.326, 118.570, 117.821, 117.076, 116.339, 115.606, 114.873, 114.146, 113.424, 112.702, 111.986, 111.275, 110.567, 109.867, 109.176, 108.488, 107.804, 107.132, 106.467, 105.809, 105.157, 104.509, 103.863, 103.225, 102.590, 101.970, 101.351, 100.740, 100.131, 99.524, 98.923, 98.331, 97.747, 97.174, 96.602, 96.037, 95.486, 94.944, 94.410, 93.889, 93.372, 92.869, 92.367, 91.876, 91.386, 90.919, 90.457, 90.005, 89.564, 89.131, 88.702, 88.296, 87.888, 87.496, 87.115, 86.750, 86.394, 86.056, 85.730, 85.410, 85.094, 84.794, 84.514, 84.258, 84.021, 83.794, 83.579, 83.384, 83.207, 83.054, 82.917, 82.801, 82.702, 82.628, 82.585, 82.571, 82.569, 82.593, 82.631, 82.703, 82.809, 82.935, 83.081, 83.271, 83.485, 83.713, 83.980, 84.274, 84.605, 84.957, 85.328, 85.749, 86.201, 86.679, 87.175, 87.739, 88.326, 88.940, 89.571, 90.272, 90.976, 91.721, 92.455, 93.245, 94.045, 94.974, 95.981, 97.024, 98.175, 99.359, 100.601, 101.879, 103.340, 104.863, 106.512, 108.257, 110.105, 111.988, 113.805, 114.410, 114.945, 116.944, 117.058, 118.446, 120.329, 119.002, 120.387, 122.186, 122.167, 123.161, 124.174, 125.479, 125.378, 126.657, 127.043, 127.319, 129.298, 127.713, 129.538, 131.443, 133.431, 132.205, 134.087, 136.081, 134.106, 136.106, 137.806, 139.777, 137.837, 139.823, 141.691, 143.218, 142.695, 144.408, 143.622, 145.007, 146.886, 147.740, 148.194, 148.660, 150.546, 152.384, 150.659, 152.350, 154.204, 155.014, 154.930, 156.282, 157.974, 156.822, 158.267, 160.062, 161.876, 163.305, 163.393, 164.314, 166.057, 166.526, 166.559, 168.057, 169.657, 169.157, 170.203, 172.145, 170.575, 172.407, 173.837, 174.812, 175.001, 176.964, 178.784, 180.348, 179.687, 181.537, 182.210, 183.834, 184.318, 185.477, 185.494, 187.369, 187.432, 188.511, 189.857, 191.559, 190.809, 192.566, 191.259, 193.064, 194.821, 195.770, 196.225, 198.218, 200.124, 198.133, 200.039, 201.953, 203.758, 202.065, 203.915, 205.836, 204.036, 206.019, 207.965, 209.667, 209.093, 210.179, 212.064, 213.094, 212.852, 214.409, 216.407, 215.088, 216.986, 218.974, 218.197, 219.893, 221.559, 222.279, 222.649, 224.301, 224.887, 226.795, 226.466, 228.357, 228.530, 229.402, 230.295, 232.260, 232.831, 233.687, 235.494, 237.213, 237.056, 237.800, 239.385, 241.080, 240.355, 241.753, 242.848, 244.802, 243.878, 245.604, 246.088, 247.833, 246.974, 248.964, 250.228, 250.545, 251.687, 253.681, 251.838, 253.807, 255.773, 254.184, 255.974, 257.793, 259.780, 258.704, 260.262, 262.229, 261.146, 262.817, 264.666, 262.692, 264.625, 266.536, 264.538, 266.502, 268.470, 266.748, 268.682, 270.358, 268.509, 270.350, 271.880, 272.544, 273.131, 273.500, 274.632, 275.035, 276.832, 274.845, 276.845, 278.830, 279.485, 281.401, 280.940, 282.581, 282.741, 284.415, 286.290, 284.988, 286.319, 288.258, 290.060, 288.400, 290.191, 291.717, 293.664, 292.889, 294.706, 296.387, 298.029, 297.674, 299.027, 300.747, 302.745, 300.976, 302.937, 304.069, 304.774, 306.309, 307.588, 307.331, 309.319, 311.092, 310.078, 311.554, 313.182, 315.117, 316.178, 317.054, 317.982, 319.981, 321.453, 319.982, 321.812, 323.607, 324.988, 325.372, 325.751, 326.889, 328.829, 327.775, 329.632, 330.770, 332.605, 330.919, 332.549, 334.362, 336.352, 334.382, 336.375, 338.371, 340.199, 342.129, 341.310, 342.932, 344.705, 346.571, 346.097, 348.092, 348.421, 349.212, 350.864, 352.716, 353.622, 354.119, 354.945, 356.906, 356.905, 357.625, 359.495, 361.271, 359.391, 361.300, 363.279, 365.119, 366.720, 366.337, 368.218, 369.014, 370.557, 370.016, 372.016, 373.387, 372.764, 374.695, 373.942, 375.456, 376.916, 378.001, 378.629, 380.621, 379.307, 381.199, 383.185, 383.243, 384.948, 384.619, 386.071, 388.007, 388.901, 390.218, 390.835, 392.619, 392.469, 394.045, 394.726, 395.812, 396.503, 396.964, 397.889, 399.479, 399.323, 401.263, 401.066, 402.418, 404.202, 404.983, 405.902, 406.509, 408.274, 407.720, 409.713, 411.169, 410.792, 411.577, 413.324, 415.324, 413.638, ])

uu = np.array([58.974, 62.949, 66.923, 70.898, 74.872, 78.846, 82.820, 86.795, 90.768, 94.740, 98.712, 102.683, 106.655, 110.628, 114.599, 118.573, 122.548, 126.523, 130.500, 134.477, 138.450, 142.426, 146.402, 150.380, 154.357, 158.337, 162.316, 166.297, 170.277, 174.256, 178.235, 182.214, 186.192, 190.168, 194.144, 198.120, 202.095, 206.069, 210.045, 214.021, 217.998, 221.976, 225.952, 229.930, 233.909, 237.890, 241.868, 245.845, 249.825, 253.801, 257.777, 261.752, 265.725, 269.699, 273.676, 277.654, 281.632, 285.605, 289.583, 293.562, 297.539, 301.519, 305.500, 309.483, 313.461, 317.443, 321.429, 325.418, 329.408, 333.401, 337.395, 341.391, 345.387, 349.385, 353.384, 357.383, 361.383, 365.383, 369.383, 373.383, 377.381, 381.379, 385.375, 389.370, 393.363, 397.353, 401.340, 405.325, 409.306, 413.285, 417.260, 421.230, 425.196, 429.155, 433.109, 437.056, 440.996, 444.928, 448.852, 452.768, 456.673, 460.567, 464.452, 468.325, 472.185, 476.031, 479.864, 483.682, 487.482, 491.265, 495.031, 498.779, 502.507, 506.209, 509.889, 513.554, 517.191, 520.798, 524.378, 527.924, 531.441, 534.920, 538.367, 541.771, 545.148, 548.478, 551.757, 554.991, 558.168, 561.282, 564.356, 567.386, 570.320, 573.199, 575.997, 578.705, 581.349, 583.854, 586.283, 588.583, 590.756, 592.796, 594.665, 596.385, 586.385, 588.695, 590.833, 592.750, 594.511, 595.926, 585.926, 588.320, 590.428, 592.132, 593.300, 594.083, 593.919, 592.521, 589.890, 585.913, 587.356, 583.514, 584.070, 580.731, 578.646, 575.660, 575.243, 573.409, 572.712, 568.716, 567.863, 565.537, 564.974, 561.291, 561.414, 558.763, 555.943, 557.703, 554.619, 550.780, 553.397, 549.994, 546.557, 542.792, 546.716, 542.738, 539.065, 535.672, 536.316, 534.837, 530.889, 532.126, 528.916, 525.472, 529.345, 525.346, 521.356, 518.061, 521.972, 518.147, 514.440, 510.842, 506.856, 510.735, 506.852, 503.592, 507.375, 503.630, 499.928, 496.302, 500.299, 496.693, 493.684, 491.558, 490.861, 488.574, 486.425, 485.703, 482.661, 486.507, 482.509, 478.536, 476.379, 475.042, 473.666, 469.788, 473.199, 469.219, 466.276, 465.290, 463.803, 460.154, 456.384, 460.383, 456.496, 455.816, 451.953, 452.205, 449.647, 448.713, 444.811, 445.349, 442.657, 441.701, 438.762, 437.722, 434.490, 435.859, 432.610, 431.735, 428.800, 426.539, 423.139, 425.154, 421.841, 417.884, 421.650, 417.663, 414.184, 418.059, 414.061, 410.144, 406.444, 410.368, 406.371, 404.459, 400.462, 401.878, 398.869, 396.788, 393.577, 395.208, 391.210, 390.740, 387.924, 387.809, 383.809, 381.619, 382.545, 381.786, 377.813, 378.285, 374.434, 375.930, 372.456, 372.420, 368.468, 366.583, 367.230, 364.572, 361.324, 363.498, 360.294, 356.639, 352.657, 356.317, 352.578, 348.748, 345.650, 349.041, 346.006, 342.008, 340.687, 337.274, 337.600, 334.189, 334.652, 331.479, 332.143, 330.844, 328.407, 325.243, 325.738, 321.825, 324.918, 321.025, 319.418, 315.557, 318.008, 314.046, 313.514, 310.987, 307.793, 311.643, 307.758, 303.883, 299.935, 301.065, 297.980, 294.030, 295.391, 291.679, 291.361, 287.367, 290.639, 286.705, 282.734, 283.016, 279.835, 279.772, 276.957, 276.279, 272.692, 274.092, 270.448, 268.888, 265.563, 264.005, 262.447, 260.889, 259.332, 257.776, 256.220, 254.666, 253.112, 251.556, 250.004, 248.451, 246.901, 245.352, 243.805, 242.260, 240.714, 239.171, 237.628, 236.085, 234.541, 232.997, 231.453, 229.911, 228.370, 226.831, 225.291, 223.751, 222.212, 220.672, 219.133, 217.592, 216.051, 214.510, 212.968, 211.425, 209.883, 208.342, 206.803, 205.265, 203.729, 202.192, 200.655, 199.117, 197.579, 196.044, 194.506, 192.968, 191.429, 189.892, 188.353, 186.814, 185.273, 183.732, 182.190, 180.651, 179.111, 177.571, 176.031, 174.489, 172.948, 171.409, 169.869, 168.330, 166.790, 165.253, 163.718, 162.184, 160.650, 159.120, 157.592, 156.064, 154.535, 153.008, 151.478, 149.947, 148.416, 146.887, 145.362, 143.835, 142.306, 140.779, 139.254, 137.734, 136.214, 134.696, 133.180, 131.667, 130.153, 128.639, 127.127, 125.620, 124.111, 122.601, 121.092, 119.584, 118.079, 116.573, 115.065, 113.557, 112.046, 110.538, 109.028, 107.520, 106.008, 104.500, 102.994, 101.487, 99.983, 98.476, 96.972, 95.471, 93.968, 92.467, 90.967, 89.470, 87.980, 86.487, 84.996, 83.502, 82.011, 80.519, 79.029, 77.540, 76.050, 74.557, 73.068, 71.584, 70.096, 68.612, 67.127, 65.641, 64.157, 62.674, 61.191, 59.711, 58.236, 56.764, 55.300, 53.828, 52.357, 50.883, 49.413, 47.949, 46.487, 45.020, 43.551, 42.085, 40.608, 39.134, 37.654, 36.182, 34.715, 33.255, 31.805, 30.352, 28.893, 27.437, 25.975, 24.509, 23.047, 21.589, 20.131, 18.678, 17.222, 15.774, 14.324, 12.886, 11.446, 10.009, 8.569, 7.136, 5.708, 4.289, 14.289, 12.706, 11.118, 9.525, 7.930, 6.329, 4.708, 14.708, 12.923, 11.317, 9.708, 8.093, 6.471, 4.838, 14.838, 13.052, 11.246, 9.431, 7.599, 6.008, 4.421, 14.421, 12.640, 10.858, 9.063, 7.257, 5.437, 3.610, 13.610, 11.671, 9.982, 8.270, 6.551, 4.816, 14.816, 12.886, 10.948, 8.998, 7.030, 5.049, 3.056, 13.056, 11.057, 9.065, 7.090, 5.157, 3.268, 13.268, 11.311, 9.401, 7.545, 5.782, 4.125, 14.125, 12.200, 10.340, 8.539, 6.878, 5.330, 4.073, 14.073, 12.088, 10.143, 8.333, 6.905, 6.213, 7.838, 7.620, 8.893, 8.561, 10.412, 8.947, 10.928, 12.106, 14.093, 12.152, 13.994, 15.097, 16.899, 15.126, 16.674, 18.365, 18.413, 19.497, 20.191, 22.127, 21.165, 23.056, 23.810, 25.693, 24.720, 26.717, 25.902, 27.847, 28.967, 28.817, 29.698, 31.170, 30.584, 31.401, 32.234, 33.099, 33.646, 35.611, 34.902, 36.572, 36.905, 38.859, 36.912, 38.909, 39.140, 40.679, 40.154, 42.123, 40.442, 42.411, 44.198, 42.301, 44.041, 45.834, 47.560, 46.582, 48.497, 48.491, 49.890, 49.940, 51.887, 51.156, 53.052, 51.542, 53.482, 54.216, 54.298, 54.995, 56.632, 55.369, 57.170, 57.682, 59.295, 58.194, 59.793, 58.244, 60.089, 60.456, 60.024, 60.632, 61.692, 63.046, 61.532, 63.516, 64.927, 63.693, 65.286, 66.499, 68.489, 67.167, 69.166, 69.774, 71.594, 70.893, 72.451, 73.492, 72.005, 73.318, 74.356, 76.125, 74.414, 76.412, 77.312, 79.275, 77.443, 79.400, 80.454, 79.561, 80.659, 82.171, 82.484, 83.231, 83.107, 84.944, 84.495, 86.178, 87.388, 89.293, 89.350, 90.983, 90.992, 92.881, 91.457, 93.455, 95.250, 93.286, 95.064, 96.802, 98.196, 97.664, 98.828, 100.309, 98.698, 100.684, 101.485, 102.020, 102.457, 103.911, 102.817, 103.856, 104.882, 106.174, 104.233, 106.168, 107.775, 108.870, 108.712, 109.292, 110.126, 109.965, 110.556, 112.173, 110.565, 111.960, 113.489, 114.137, 114.657, 115.137, 117.033, 116.674, 118.674, 117.276, 119.266, 118.726, 120.686, 121.111, 121.587, 122.047, 123.318, 122.796, 123.502, 124.560, 126.541, 125.249, 127.240, 125.926, 127.894, 127.276, 129.266, 128.238, 130.218, 129.141, 130.950, 132.780, 132.800, 134.248, 134.779, 135.109, 135.467, 136.443, 137.487, 137.484, 139.484, 138.307, 140.279, 141.297, 141.990, 142.098, 143.735, 142.208, 143.943, 144.865, 146.417, 145.327, 146.316, 147.497, 149.417, 147.862, 149.782, 151.319, 149.324, 151.311, 153.220, 155.210, 154.177, 156.123, 155.624, 157.562, 156.851, 158.642, 158.022, 159.953, 160.149, 161.757, 159.931, 161.345, 162.654, 164.407, 166.401, 165.599, 167.598, 166.581, 168.412, 170.230, 168.235, 170.182, 171.557, 172.667, 172.842, 173.237, 174.375, 176.333, 175.078, 177.055, 178.724, 176.768, 178.627, 180.276, 181.501, 181.161, 181.915, 183.736, 183.104, 185.028, 183.038, 184.792, 186.245, 188.195, 186.772, 188.768, 190.689, 190.153, 191.579, 192.483, 192.790, 193.528, 195.514, 193.878, 195.867, 197.000, 197.102, 197.698, 198.775, 200.745, 199.201, 201.153, 202.762, 201.525, 203.457, 204.129, 206.059, 204.380, 206.325, 206.743, 206.242, 207.002, 208.248, 210.192, 208.545, 210.344, 211.247, 211.204, 212.422, 213.498, 212.975, 214.448, 216.042, 218.028, 216.232, 218.184, 219.410, 221.362, 220.412, 221.949, 222.538, 222.068, 223.312, 224.630, 225.250, 225.173, 226.178, 228.008, 226.102, 228.092, 229.435, 228.282, 230.122, 230.718, 232.477, 231.143, 232.790, 230.793, 232.481, 233.478, 234.157, 234.152, 235.700, 237.362, 236.105, 237.449, 238.843, 240.722, 239.723, 241.149, 240.646, 242.105, 240.498, 242.125, 243.297, 245.209, 243.358, 245.349, 247.227, 245.253, 246.927, 248.895, 247.475, 249.395, 250.948, 249.251, 251.249, 252.642, 252.782, 253.687, 254.084, 255.842, 254.023, 256.014, 257.804, 259.719, 258.704, 260.513, 260.910, 262.606, 261.176, 262.734, 264.255, 265.475, 266.297, 266.270, 268.195, 267.133, 268.315, 269.547, 270.196, 270.924, 271.619, 271.379, 273.093, 272.641, 274.476, 274.128, 275.800, 274.933, 276.854, 276.716, 278.350, 278.298, 279.984, 279.215, 281.215, 280.402, 282.232, 281.546, 283.433, 283.027, 285.026, 285.267, 285.905, 287.131, 289.030, 287.038, 288.821, 290.418, 292.031, 290.051, 291.954, 293.686, 291.686, 293.626, 295.111, 297.080, 295.095, 296.809, 298.764, 296.787, 298.779, 300.568, 300.570, 302.014, 302.480, 304.412, 304.032, 305.920, 306.450, 308.257, 307.685, 309.669, 308.865, 310.863, 309.724, 311.696, 310.035, 311.997, 312.553, 312.727, 313.184, 314.974, 315.331, 316.916, 316.543, 318.031, 318.082, 319.062, 319.465, 321.408, 319.520, 321.285, 319.980, 321.945, 321.728, 323.408, 323.105, 324.987, 324.618, 325.205, 324.366, 325.364, 326.310, 328.182, 326.186, 327.591, 328.067, 330.062, 329.248, 331.153, 331.192, 333.095, 331.906, 333.890, 332.541, 334.500, 335.977, 334.285, 336.245, 337.342, 339.184, 337.185, 338.839, 340.203, 338.841, 340.033, 341.301, 342.683, 340.698, 342.308, 342.578, 344.475, 342.995, 344.950, 344.674, 346.658, 344.752, 346.706, 347.027, 348.628, 348.345, 350.080, 348.154, 349.667, 351.228, 352.326, 350.766, 352.541, 353.776, 352.819, 353.794, 355.319, 357.274, 356.247, 358.247, 356.761, 358.737, 357.561, 359.487, 358.414, 359.512, 357.730, 359.721, 361.062, 361.728, 362.312, 362.589, 364.230, 365.011, 365.676, 366.164, 367.256, 369.242, 368.340, 369.272, 370.350, 371.422, 373.299, 372.751, 374.706, 376.699, 375.229, 377.122, 379.007, 380.824, 379.977, 381.977, 382.014, 382.582, 383.398, 384.735, 383.212, 385.170, 385.623, 387.581, 386.749, 388.656, 387.837, 389.674, 389.853, 391.242, 391.420, 393.246, 392.316, 394.254, 393.163, 395.156, 395.805, 396.349, 397.919, 399.114, 398.618, 399.311, 401.075, 400.074, 401.866, 402.266, 404.013, 403.955, 405.906, 403.922, 405.306, 406.942, 407.795, 407.956, 409.804, 408.452, 410.446, 411.028, 412.663, 411.091, 412.053, 414.027, 412.560, 414.532, 416.223, 418.172, 416.519, 418.498, 419.926, 421.655, 421.056, 423.025, 421.770, 423.662, 422.519, 424.484, 424.495, 426.456, 424.787, 424.943, 426.884, ])
vv = np.array([555.458, 555.904, 556.353, 556.807, 557.255, 557.710, 558.173, 558.618, 559.083, 559.553, 560.021, 560.508, 560.981, 561.440, 561.922, 562.376, 562.827, 563.269, 563.702, 564.132, 564.590, 565.034, 565.468, 565.890, 566.310, 566.719, 567.120, 567.513, 567.908, 568.319, 568.728, 569.142, 569.563, 569.997, 570.434, 570.875, 571.322, 571.775, 572.211, 572.650, 573.078, 573.497, 573.937, 574.355, 574.762, 575.156, 575.571, 575.999, 576.399, 576.834, 577.275, 577.722, 578.182, 578.637, 579.067, 579.485, 579.908, 580.367, 580.785, 581.194, 581.625, 582.027, 582.415, 582.787, 583.205, 583.583, 583.915, 584.218, 584.492, 584.735, 584.950, 585.135, 585.300, 585.431, 585.532, 585.598, 585.631, 585.629, 585.596, 585.528, 585.426, 585.291, 585.119, 584.913, 584.670, 584.391, 584.075, 583.724, 583.336, 582.928, 582.481, 581.994, 581.468, 580.902, 580.294, 579.643, 578.953, 578.221, 577.446, 576.628, 575.763, 574.849, 573.895, 572.894, 571.846, 570.747, 569.604, 568.410, 567.161, 565.863, 564.515, 563.117, 561.668, 560.152, 558.584, 556.982, 555.316, 553.588, 551.803, 549.953, 548.047, 546.074, 544.043, 541.943, 539.800, 537.584, 535.293, 532.938, 530.508, 527.998, 525.438, 522.826, 520.109, 517.331, 514.472, 511.529, 508.527, 505.408, 502.230, 498.958, 495.599, 492.159, 488.622, 485.011, 481.345, 478.079, 474.698, 471.187, 467.596, 463.855, 460.001, 456.797, 453.397, 449.778, 445.952, 442.030, 438.033, 434.285, 431.273, 430.846, 427.115, 428.230, 424.269, 426.471, 423.058, 425.720, 421.742, 425.297, 421.358, 421.193, 417.285, 420.539, 416.579, 418.139, 414.141, 417.136, 414.299, 410.707, 413.254, 412.132, 409.107, 411.209, 409.162, 407.813, 407.036, 406.615, 405.031, 402.912, 406.860, 403.143, 402.500, 398.696, 401.083, 399.048, 398.046, 397.968, 398.255, 395.988, 396.829, 395.656, 394.155, 392.406, 392.070, 391.094, 390.134, 387.817, 389.116, 387.709, 386.195, 384.506, 384.335, 382.603, 379.967, 383.355, 379.416, 376.135, 379.508, 375.574, 372.977, 371.880, 371.778, 372.245, 368.876, 372.646, 368.890, 367.910, 365.820, 366.228, 363.519, 359.643, 363.356, 361.717, 360.381, 360.337, 359.393, 355.451, 356.488, 352.496, 355.571, 351.682, 352.562, 348.598, 351.556, 347.672, 350.385, 346.523, 344.166, 347.925, 345.591, 341.688, 344.405, 341.106, 343.212, 339.757, 337.515, 336.926, 335.577, 335.252, 333.279, 332.287, 332.164, 331.355, 329.835, 329.059, 328.912, 325.399, 325.242, 321.501, 324.138, 320.722, 323.108, 319.455, 319.602, 315.630, 318.471, 314.472, 314.401, 317.748, 313.857, 309.929, 310.398, 306.425, 307.507, 303.797, 305.778, 301.779, 301.158, 304.686, 300.739, 297.749, 295.415, 298.773, 296.378, 294.753, 294.368, 295.982, 294.561, 293.407, 290.876, 292.998, 290.393, 290.253, 286.478, 288.564, 284.577, 286.666, 282.693, 280.257, 284.202, 280.419, 277.246, 279.693, 275.723, 274.893, 272.357, 273.276, 269.614, 270.657, 267.496, 266.946, 262.982, 266.082, 263.674, 264.761, 263.807, 262.816, 262.171, 258.334, 260.880, 260.251, 256.490, 257.980, 253.993, 254.225, 251.923, 252.651, 252.172, 248.182, 250.608, 246.608, 243.766, 247.708, 245.939, 242.192, 243.841, 242.590, 240.366, 239.113, 237.858, 236.604, 235.349, 234.093, 232.836, 231.577, 230.319, 229.061, 227.801, 226.540, 225.276, 224.011, 222.743, 221.473, 220.204, 218.932, 217.660, 216.388, 215.115, 213.844, 212.573, 211.299, 210.024, 208.748, 207.472, 206.195, 204.918, 203.642, 202.365, 201.089, 199.814, 198.540, 197.266, 195.994, 194.720, 193.445, 192.168, 190.890, 189.608, 188.328, 187.049, 185.771, 184.492, 183.211, 181.931, 180.653, 179.376, 178.096, 176.818, 175.541, 174.266, 172.992, 171.718, 170.441, 169.165, 167.888, 166.613, 165.339, 164.063, 162.787, 161.510, 160.233, 158.957, 157.677, 156.396, 155.112, 153.829, 152.540, 151.250, 149.960, 148.670, 147.379, 146.091, 144.804, 143.517, 142.228, 140.934, 139.643, 138.353, 137.061, 135.767, 134.468, 133.168, 131.865, 130.561, 129.253, 127.946, 126.640, 125.330, 124.016, 122.703, 121.391, 120.079, 118.765, 117.448, 116.132, 114.818, 113.505, 112.194, 110.881, 109.569, 108.255, 106.946, 105.632, 104.317, 103.001, 101.683, 100.368, 99.049, 97.728, 96.408, 95.086, 93.764, 92.438, 91.103, 89.773, 88.440, 87.110, 85.777, 84.445, 83.111, 81.775, 80.441, 79.111, 77.775, 76.435, 75.098, 73.757, 72.418, 71.080, 69.739, 68.397, 67.055, 65.709, 64.359, 63.005, 61.642, 60.288, 58.934, 57.581, 56.226, 54.863, 53.498, 52.139, 50.781, 49.421, 48.073, 46.721, 45.375, 44.022, 42.662, 41.295, 39.918, 38.543, 37.175, 35.804, 34.439, 33.079, 31.714, 30.345, 28.976, 27.602, 26.230, 24.851, 23.474, 22.084, 20.695, 19.305, 17.916, 16.521, 15.121, 13.711, 12.287, 11.064, 9.849, 8.639, 7.433, 6.235, 5.062, 3.910, 13.910, 12.717, 11.530, 10.351, 9.181, 8.026, 6.865, 5.964, 5.104, 4.265, 14.265, 13.052, 11.835, 10.630, 9.720, 8.813, 7.932, 7.072, 6.242, 5.430, 4.623, 14.623, 13.552, 12.518, 11.496, 10.502, 9.558, 9.033, 8.537, 8.094, 7.738, 7.464, 7.293, 7.281, 7.327, 7.510, 7.826, 8.340, 8.997, 9.839, 10.249, 10.841, 11.588, 12.533, 13.653, 15.052, 15.593, 16.329, 17.199, 18.313, 19.579, 21.135, 23.032, 23.277, 23.744, 24.593, 25.994, 27.870, 29.037, 31.025, 29.483, 31.455, 32.212, 33.574, 33.303, 34.920, 35.146, 35.630, 36.409, 38.078, 38.944, 38.021, 39.287, 40.354, 42.354, 40.673, 42.548, 43.048, 44.801, 44.151, 46.003, 45.327, 47.075, 46.967, 48.794, 48.325, 49.982, 47.987, 49.783, 51.137, 49.225, 51.050, 52.868, 51.065, 52.989, 53.362, 55.232, 54.132, 56.104, 56.529, 56.987, 57.105, 59.091, 57.815, 59.744, 60.095, 61.180, 60.829, 61.728, 61.095, 62.080, 62.966, 63.976, 65.721, 65.144, 67.144, 65.714, 67.713, 67.255, 69.117, 69.753, 71.065, 71.552, 73.412, 71.414, 73.288, 74.438, 75.988, 75.120, 77.053, 75.870, 77.540, 78.743, 80.008, 79.236, 81.202, 79.249, 81.154, 82.850, 84.322, 85.629, 85.377, 86.795, 85.220, 86.430, 88.019, 88.226, 89.727, 89.684, 91.589, 90.760, 92.633, 93.888, 95.595, 94.258, 95.767, 97.476, 98.408, 99.442, 99.370, 101.156, 101.537, 102.339, 102.752, 104.452, 102.662, 104.334, 105.643, 107.619, 105.764, 107.760, 108.552, 110.502, 109.421, 111.013, 111.622, 113.621, 112.466, 114.466, 115.125, 116.529, 116.616, 117.499, 117.118, 118.034, 119.024, 120.458, 118.530, 120.157, 121.501, 122.687, 122.448, 124.280, 122.353, 124.305, 125.678, 124.004, 125.713, 127.429, 128.956, 128.475, 128.979, 130.170, 131.843, 129.850, 131.764, 133.581, 131.588, 133.499, 134.675, 133.486, 134.919, 136.208, 138.100, 136.169, 138.111, 137.475, 139.442, 139.448, 140.878, 141.079, 143.005, 142.605, 144.559, 142.617, 144.563, 146.108, 144.177, 146.048, 147.746, 147.469, 148.996, 148.810, 150.318, 149.960, 151.862, 151.659, 153.375, 153.089, 154.775, 153.921, 154.726, 156.726, 155.347, 157.275, 155.303, 157.270, 159.016, 157.310, 159.310, 159.305, 160.921, 160.592, 162.314, 160.438, 162.435, 163.585, 162.293, 163.288, 165.063, 166.324, 164.647, 166.386, 168.000, 168.561, 169.819, 170.377, 171.657, 171.790, 172.011, 172.609, 172.808, 174.520, 174.059, 175.996, 175.502, 177.371, 178.260, 180.162, 179.639, 181.630, 182.819, 182.003, 183.418, 184.930, 185.892, 185.739, 187.570, 187.626, 189.348, 188.545, 189.380, 189.235, 189.690, 191.143, 192.807, 190.815, 192.775, 194.420, 194.013, 195.570, 195.876, 196.978, 196.561, 197.297, 198.429, 196.848, 198.819, 200.671, 199.843, 201.740, 202.284, 202.479, 203.440, 204.815, 204.370, 205.776, 205.909, 206.466, 208.392, 206.990, 208.775, 206.798, 208.657, 208.423, 209.575, 209.784, 211.432, 209.435, 211.344, 213.030, 213.372, 214.643, 214.207, 215.394, 216.966, 216.449, 218.333, 218.857, 219.944, 220.411, 222.367, 220.431, 222.281, 223.845, 223.377, 224.512, 225.386, 223.602, 225.601, 227.188, 228.874, 226.943, 228.297, 229.504, 229.739, 230.619, 231.058, 232.638, 232.204, 233.964, 235.243, 237.154, 235.210, 236.776, 238.281, 236.380, 238.378, 240.108, 240.913, 241.517, 241.715, 243.197, 244.832, 244.048, 245.957, 245.005, 246.495, 247.630, 247.739, 248.811, 250.545, 248.664, 250.664, 251.930, 253.043, 251.488, 252.969, 254.403, 253.719, 255.451, 254.048, 255.984, 257.353, 256.162, 257.325, 258.946, 259.532, 260.289, 260.481, 261.167, 260.845, 261.941, 262.294, 263.703, 263.143, 264.404, 265.461, 265.386, 266.822, 264.827, 266.610, 268.570, 269.525, 270.356, 270.542, 271.434, 272.011, 273.734, 272.882, 274.843, 275.903, 274.505, 275.759, 277.058, 278.642, 276.819, 278.819, 279.363, 277.668, 279.281, 280.857, 282.749, 280.886, 282.761, 284.747, 283.716, 285.665, 286.461, 288.430, 287.332, 289.135, 288.577, 290.572, 289.418, 291.417, 290.341, 292.188, 292.222, 294.049, 293.242, 295.121, 294.458, 296.417, 296.347, 298.332, 296.437, 298.017, 298.644, 298.473, 299.378, 300.582, 301.765, 301.481, 302.097, 303.097, 303.143, 303.632, 304.971, 305.323, 305.570, 306.601, 307.026, 307.329, 307.502, 308.396, 310.396, 309.012, 310.957, 310.443, 312.407, 311.747, 313.676, 312.818, 314.734, 314.986, 316.817, 316.902, 318.546, 318.877, 319.991, 320.381, 322.302, 320.310, 322.257, 323.150, 325.118, 323.899, 325.864, 327.200, 329.200, 327.456, 329.415, 329.889, 330.548, 331.488, 333.004, 332.633, 334.621, 333.536, 335.513, 334.837, 336.802, 338.714, 336.899, 338.631, 340.394, 341.098, 340.976, 342.399, 344.342, 344.198, 346.026, 345.414, 347.413, 346.798, 348.406, 348.148, 349.625, 349.223, 350.572, 351.638, 351.239, 352.911, 353.689, 353.733, 354.857, 356.320, 354.856, 356.462, 358.008, 359.455, 359.204, 360.391, 362.373, 361.738, 363.084, 362.661, 364.641, 364.892, 365.499, 365.927, 367.901, 366.703, 368.682, 369.676, 369.138, 370.447, 371.696, 373.368, 372.116, 373.038, 374.611, 372.855, 374.602, 375.895, 375.471, 377.188, 377.168, 378.506, 378.198, 379.815, 379.276, 380.964, 382.636, 383.545, 383.739, 385.223, 387.108, 385.195, 387.176, 388.319, 390.161, 388.275, 390.214, 391.890, 392.120, 390.335, 392.105, 393.789, 395.478, 394.790, 396.713, 397.135, 397.305, 398.661, 398.016, 398.685, 397.847, 399.659, 399.694, 401.694, 399.776, 401.602, 403.089, 404.385, 403.977, 405.926, 405.516, 407.335, 407.937, 409.762, 408.971, 410.963, 409.524, 411.516, 410.702, 412.472, 412.965, 414.641, 414.481, 416.373, 414.449, 415.688, 414.084, 416.021, 417.897, 416.955, 418.686, 417.799, 419.759, 418.785, 420.785, 421.222, 421.470, 422.914, 424.064, 422.255, 424.249, 425.014, 426.488, 426.648, 428.562, 429.715, 428.478, 430.231, 430.552, 431.911, 431.576, 432.645, 433.095, 434.220, 433.936, 435.337, 434.334, 436.242, 436.595, 438.152, 438.799, 440.440, 440.071, 442.071, 442.466, 443.567, 445.561, 445.080, ])

plt.plot(xx, 600 - yy, c='silver', label='MDAF', linewidth=1, zorder=2)
plt.plot(uu, 600 - vv, '-.', c='#CDAA7D', label='SPPL', linewidth=1, zorder=2)

n = 50
X = list()
for i in range(n-1):
    np.random.seed(i)
    x = np.random.randint(100, 300)
    y = np.random.randint(100, 300)
    X.append([x, y])

# 离群点的特殊的一只羊,在目标区域
Y = np.array([550, 50])

X = np.array(X)
plt.scatter(X[:, 0], 600-X[:, 1], c='blue', label="normal sheep", zorder=3)
plt.scatter(Y[0], Y[1], c='green', label="outlier sheep", zorder=3)
plt.xlabel("X Position")
plt.ylabel("Y Position")

range_x = np.arange(0, 700, 100)
plt.xticks(range_x)
plt.yticks(range_x)
# plt.grid()
plt.legend()
plt.show()
fig.savefig('E:\\我的坚果云\\latex\\doubleDistSum\\pics\\sppl_mdaf_trajectory_outlier_target.pdf', dpi=600, format='pdf')
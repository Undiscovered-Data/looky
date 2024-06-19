#!/usr/bin/python3


Abilene_r = {"Amarillo": 266, "Austin": 213, "Beaumont": 412, "Big Bend": 392, "Big Spring": 107, "Brownsville": 516, "Brownwood": 77, "Bryan": 253, "Childress": 154, "Corpus Christi": 387, "Dalhart": 343,  "Dallas": 180, "Del Rio": 246, "Denison": 235, "Eagle Pass": 298,  "El Paso": 439, "Fort Stockton": 250, "Fort Worth": 150, "Gainsville": 195, "Galveston": 398, "Houston": 348, "Huntsville": 304, "Junction": 144, "Kingsville": 397, "Laredo": 373, "Longview": 305, "Lubbock": 162, "Lufkin": 336, "McAllen": 480, "Odessa": 167, "Orange": 434, "Ozona": 170, "Paris": 281, "Pecos": 240, "San Angelo": 89, "San Antonio": 244, "South Padre Is": 530, "Temple": 181, "Texarkana": 359, "Tyler": 277, "Van Horn": 328, "Victoria": 334, "Waco": 183, "Wichita Falls": 141, "Yoakum": 304}

Amarillo_r = {"Austin": 478, "Beaumont": 637, "Big Bend": 484, "Big Spring": 222, "Brownsville": 765, "Brownwood": 342, "Bryan": 503, "Childress": 116, "Corpus Christi": 636, "Dalhart": 82,  "Dallas": 361, "Del Rio": 450, "Denison": 348, "Eagle Pass": 505,  "El Paso": 418, "Fort Stockton": 338, "Fort Worth": 337, "Gainsville": 309, "Galveston": 646, "Houston": 596, "Huntsville": 528, "Junction": 380, "Kingsville": 646, "Laredo": 609, "Longview": 482, "Lubbock": 119, "Lufkin": 529, "McAllen": 728, "Odessa": 255, "Orange": 649, "Ozona": 336, "Paris": 403, "Pecos": 320, "San Angelo": 293, "San Antonio": 493, "South Padre Is": 779, "Temple": 444, "Texarkana": 495, "Tyler": 457, "Van Horn": 401, "Victoria": 600, "Waco": 423, "Wichita Falls": 225, "Yoakum": 566}

Austin_r = {"Beaumont": 238, "Big Bend": 462, "Big Spring": 289, "Brownsville": 325, "Brownwood": 137, "Bryan": 100, "Childress": 367, "Corpus Christi": 192, "Dalhart": 556,  "Dallas": 192, "Del Rio": 232, "Denison": 267, "Eagle Pass": 220,  "El Paso": 573, "Fort Stockton": 335, "Fort Worth": 187, "Gainsville": 252, "Galveston": 206, "Houston": 162, "Huntsville": 153, "Junction": 139, "Kingsville": 206, "Laredo": 232, "Longview": 256, "Lubbock": 368, "Lufkin": 219, "McAllen": 300, "Odessa": 334, "Orange": 262, "Ozona": 229, "Paris": 294, "Pecos": 388, "San Angelo": 203, "San Antonio": 79, "South Padre Is": 339, "Temple": 67, "Texarkana": 340, "Tyler": 224, "Van Horn": 454, "Victoria": 122, "Waco": 102, "Wichita Falls": 283, "Yoakum": 88}

Beaumont_r = {"Big Bend": 699, "Big Spring": 519, "Brownsville": 437, "Brownwood": 350, "Bryan": 158, "Childress": 521, "Corpus Christi": 288, "Dalhart": 719,  "Dallas": 276, "Del Rio": 434, "Denison": 321, "Eagle Pass": 421,  "El Paso": 810, "Fort Stockton": 572, "Fort Worth": 301, "Gainsville": 345, "Galveston": 78, "Houston": 86, "Huntsville": 113, "Junction": 376, "Kingsville": 317, "Laredo": 396, "Longview": 194, "Lubbock": 574, "Lufkin": 108, "McAllen": 430, "Odessa": 567, "Orange": 24, "Ozona": 466, "Paris": 292, "Pecos": 625, "San Angelo": 436, "San Antonio": 281, "South Padre Is": 451, "Temple": 230, "Texarkana": 256, "Tyler": 192, "Van Horn": 690, "Victoria": 209, "Waco": 242, "Wichita Falls": 412, "Yoakum": 204}

Big_Bend_r = {"Big Spring": 281, "Brownsville": 636, "Brownwood": 398, "Bryan": 559, "Childress": 483, "Corpus Christi": 524, "Dalhart": 525,  "Dallas": 559, "Del Rio": 253, "Denison": 606, "Eagle Pass": 309,  "El Paso": 329, "Fort Stockton": 139, "Fort Worth": 529, "Gainsville": 584, "Galveston": 651, "Houston": 603, "Huntsville": 602, "Junction": 332, "Kingsville": 602, "Laredo": 434, "Longview": 649, "Lubbock": 360, "Lufkin": 675, "McAllen": 578, "Odessa": 222, "Orange": 715, "Ozona": 236, "Paris": 665, "Pecos": 190, "San Angelo": 300, "San Antonio": 406, "South Padre Is": 644, "Temple": 499, "Texarkana": 744, "Tyler": 647, "Van Horn": 199, "Victoria": 522, "Waco": 518, "Wichita Falls": 213, "Yoakum": 460}

Big_Spring_r = {"Brownsville": 567, "Brownwood": 174, "Bryan": 360, "Childress": 204, "Corpus Christi": 438, "Dalhart": 294,  "Dallas": 287, "Del Rio": 231, "Denison": 341, "Eagle Pass": 286,  "El Paso": 332, "Fort Stockton": 143, "Fort Worth": 257, "Gainsville": 301, "Galveston": 493, "Houston": 449, "Huntsville": 411, "Junction": 182, "Kingsville": 448, "Laredo": 406, "Longview": 412, "Lubbock": 104, "Lufkin": 443, "McAllen": 531, "Odessa": 60, "Orange": 541, "Ozona": 117, "Paris": 388, "Pecos": 133, "San Angelo": 87, "San Antonio": 295, "South Padre Is": 251, "Temple": 288, "Texarkana": 466, "Tyler": 384, "Van Horn": 221, "Victoria": 402, "Waco": 290, "Wichita Falls": 234, "Yoakum": 368}

Brownsville_r = {"Brownwood": 471, "Bryan": 382, "Childress": 671, "Corpus Christi": 159, "Dalhart": 842,  "Dallas": 517, "Del Rio": 378, "Denison": 592, "Eagle Pass": 324,  "El Paso": 801, "Fort Stockton": 563, "Fort Worth": 512, "Gainsville": 577, "Galveston": 374, "Houston": 352, "Huntsville": 414, "Junction": 386, "Kingsville": 119, "Laredo": 199, "Longview": 557, "Lubbock": 655, "Lufkin": 470, "McAllen": 56, "Odessa": 609, "Orange": 459, "Ozona": 476, "Paris": 615, "Pecos": 616, "San Angelo": 481, "San Antonio": 272, "South Padre Is": 27, "Temple": 392, "Texarkana": 634, "Tyler": 526, "Van Horn": 682, "Victoria": 230, "Waco": 427, "Wichita Falls": 608, "Yoakum": 259}

Brownwood_r = {"Bryan": 191, "Childress": 231, "Corpus Christi": 329, "Dalhart": 420,  "Dallas": 157, "Del Rio": 231, "Denison": 221, "Eagle Pass": 260,  "El Paso": 493, "Fort Stockton": 260, "Fort Worth": 127, "Gainsville": 185, "Galveston": 336, "Houston": 286, "Huntsville": 241, "Junction": 107, "Kingsville": 340, "Laredo": 330, "Longview": 278, "Lubbock": 232, "Lufkin": 274, "McAllen": 423, "Odessa": 219, "Orange": 372, "Ozona": 178, "Paris": 257, "Pecos": 293, "San Angelo": 96, "San Antonio": 187, "South Padre Is": 473, "Temple": 119, "Texarkana": 335, "Tyler": 242, "Van Horn": 378, "Victoria": 259, "Waco": 123, "Wichita Falls": 169, "Yoakum": 226}

Bryan_r = {"Childress": 388, "Corpus Christi": 237, "Dalhart": 503,  "Dallas": 165, "Del Rio": 318, "Denison": 237, "Eagle Pass": 306,  "El Paso": 660, "Fort Stockton": 422, "Fort Worth": 167, "Gainsville": 232, "Galveston": 145, "Houston": 95, "Huntsville": 54, "Junction": 237, "Kingsville": 263, "Laredo": 318, "Longview": 177, "Lubbock": 415, "Lufkin": 121, "McAllen": 364, "Odessa": 408, "Orange": 181, "Ozona": 325, "Paris": 234, "Pecos": 475, "San Angelo": 277, "San Antonio": 165, "South Padre Is": 396, "Temple": 72, "Texarkana": 261, "Tyler": 145, "Van Horn": 540, "Victoria": 152, "Waco": 85, "Wichita Falls": 270, "Yoakum": 124}

Childress_r = {"Corpus Christi": 542, "Dalhart": 197,  "Dallas": 245, "Del Rio": 382, "Denison": 232, "Eagle Pass": 437,  "El Paso": 482, "Fort Stockton": 347, "Fort Worth": 222, "Gainsville": 193, "Galveston": 531, "Houston": 480, "Huntsville": 412, "Junction": 299, "Kingsville": 552, "Laredo": 528, "Longview": 366, "Lubbock": 139, "Lufkin": 414, "McAllen": 634, "Odessa": 263, "Orange": 533, "Ozona": 300, "Paris": 287, "Pecos": 337, "San Angelo": 225, "San Antonio": 398, "South Padre Is": 684, "Temple": 329, "Texarkana": 379, "Tyler": 342, "Van Horn": 425, "Victoria": 489, "Waco": 307, "Wichita Falls": 109, "Yoakum": 455}

Corpus_Christi_r = {"Dalhart": 713,  "Dallas": 377, "Del Rio": 268, "Denison": 452, "Eagle Pass": 218,  "El Paso": 691, "Fort Stockton": 453, "Fort Worth": 372, "Gainsville": 437, "Galveston": 219, "Houston": 207, "Huntsville": 269, "Junction": 257, "Kingsville": 39, "Laredo": 141, "Longview": 411, "Lubbock": 526, "Lufkin": 325, "McAllen": 152, "Odessa": 480, "Orange": 310, "Ozona": 347, "Paris": 470, "Pecos": 506, "San Angelo": 352, "San Antonio": 143, "South Padre Is": 172, "Temple": 255, "Texarkana": 489, "Tyler": 381, "Van Horn": 571, "Victoria": 85, "Waco": 287, "Wichita Falls": 474, "Yoakum": 115}

Dalhart_r = {"Dallas": 443, "Del Rio": 520, "Denison": 429, "Eagle Pass": 575,  "El Paso": 417, "Fort Stockton": 398, "Fort Worth": 419, "Gainsville": 391, "Galveston": 728, "Houston": 678, "Huntsville": 610, "Junction": 457, "Kingsville": 723, "Laredo": 686, "Longview": 564, "Lubbock": 196, "Lufkin": 611, "McAllen": 806, "Odessa": 315, "Orange": 731, "Ozona": 406, "Paris": 485, "Pecos": 374, "San Angelo": 371, "San Antonio": 570, "South Padre Is": 856, "Temple": 524, "Texarkana": 576, "Tyler": 539, "Van Horn": 447, "Victoria": 677, "Waco": 504, "Wichita Falls": 307, "Yoakum": 643}

Dallas_r = {"Del Rio": 388, "Denison": 75, "Eagle Pass": 412,  "El Paso": 617, "Fort Stockton": 416, "Fort Worth": 30, "Gainsville": 69, "Galveston": 288, "Houston": 238, "Huntsville": 170, "Junction": 264, "Kingsville": 398, "Laredo": 424, "Longview": 125, "Lubbock": 322, "Lufkin": 168, "McAllen": 491, "Odessa": 347, "Orange": 288, "Ozona": 334, "Paris": 103, "Pecos": 420, "San Angelo": 252, "San Antonio": 271, "South Padre Is": 531, "Temple": 126, "Texarkana": 178, "Tyler": 97, "Van Horn": 508, "Victoria": 292, "Waco": 91, "Wichita Falls": 136, "Yoakum": 266}

Del_Rio_r = {"Denison": 452,"Eagle Pass": 55,"El Paso": 424,"Fort Stockton": 185,"Fort Worth": 358, "Gainsville": 416,"Galveston": 393,"Houston": 349,"Huntsville": 369,"Junction": 124, "Kingsville": 260, "Laredo": 179, "Longview": 488, "Lubbock": 332, "Lufkin": 439, "McAllen": 322, "Odessa": 247, "Orange": 455, "Ozona": 114, "Paris": 488, "Pecos": 238, "San Angelo": 158, "San Antonio": 154, "South Padre Is": 392, "Temple": 299, "Texarkana": 566, "Tyler": 455, "Van Horn": 304, "Victoria": 264, "Waco": 334, "Wichita Falls": 388, "Yoakum": 246}

Denison_r = {"Eagle Pass": 481, "El Paso": 666, "Fort Stockton": 479, "Fort Worth": 94, "Gainsville": 40, "Galveston": 361, "Houston": 310, "Huntsville": 242, "Junction": 328, "Kingsville": 473, "Laredo": 499, "Longview": 150, "Lubbock": 328, "Lufkin": 213, "McAllen": 566, "Odessa": 401, "Orange": 333, "Ozona": 397, "Paris": 65, "Pecos": 474, "San Angelo": 315, "San Antonio": 346, "South Padre Is": 606, "Temple": 201, "Texarkana": 157, "Tyler": 130, "Van Horn": 562, "Victoria": 367, "Waco": 166, "Wichita Falls": 123, "Yoakum": 339}

Eagle_Pass_r = {"El Paso": 478, "Fort Stockton": 240,"Fort Worth": 387, "Gainsville": 446, "Galveston": 380, "Houston": 336, "Huntsville": 357, "Junction": 154, "Kingsville": 205, "Laredo": 124, "Longview": 476, "Lubbock": 387, "Lufkin": 427, "McAllen": 268, "Odessa": 301, "Orange": 443, "Ozona": 169, "Paris": 515, "Pecos": 493, "San Angelo": 212, "San Antonio": 142, "South Padre Is": 338, "Temple": 287, "Texarkana": 559, "Tyler": 443, "Van Horn": 359, "Victoria": 241, "Waco": 322, "Wichita Falls": 429, "Yoakum": 233}

El_Paso_r = {"Fort Stockton": 238, "Fort Worth": 587, "Gainsville": 625, "Galveston": 774, "Houston": 730, "Huntsville": 714, "Junction": 435, "Kingsville": 683, "Laredo": 602, "Longview": 742, "Lubbock": 344, "Lufkin": 761, "McAllen": 745, "Odessa": 274, "Orange": 834, "Ozona": 344, "Paris": 717, "Pecos": 207, "San Angelo": 402, "San Antonio": 548, "South Padre Is": 815, "Temple": 595, "Texarkana": 795, "Tyler": 714, "Van Horn": 119, "Victoria": 661, "Waco": 610, "Wichita Falls": 552, "Yoakum": 630}

Fort_Stockton_r = {"Fort Worth": 385, "Gainsville": 439, "Galveston": 536, "Houston": 492, "Huntsville": 475, "Junction": 197, "Kingsville": 445, "Laredo": 364, "Longview": 535, "Lubbock": 220, "Lufkin": 523, "McAllen": 507, "Odessa": 83, "Orange": 596, "Ozona": 106, "Paris": 516, "Pecos": 53, "San Angelo": 164, "San Antonio": 310, "South Padre Is": 577, "Temple": 357, "Texarkana": 594, "Tyler": 500, "Van Horn": 119, "Victoria": 423, "Waco": 372, "Wichita Falls": 376, "Yoakum": 395}

Fort_Worth_r = {"Gainsville": 65, "Galveston": 309, "Houston": 259, "Huntsville": 191, "Junction": 233, "Kingsville": 393, "Laredo": 416, "Longview": 155, "Lubbock": 292, "Lufkin": 199, "McAllen": 486, "Odessa": 317, "Orange": 318, "Ozona": 303, "Paris": 131, "Pecos": 390, "San Angelo": 222, "San Antonio": 262, "South Padre Is": 526, "Temple": 121, "Texarkana": 209, "Tyler": 127, "Van Horn": 478, "Victoria": 287, "Waco": 86, "Wichita Falls": 112, "Yoakum": 260}

Gainsville_r = {"Galveston": 358, "Houston": 307, "Huntsville": 239, "Junction": 292, "Kingsville": 458, "Laredo": 480, "Longview": 178, "Lubbock": 290, "Lufkin": 238, "McAllen": 551, "Odessa": 360, "Orange": 358, "Ozona": 357, "Paris": 96, "Pecos": 434, "San Angelo": 275, "San Antonio": 326, "South Padre Is": 591, "Temple": 186, "Texarkana": 188, "Tyler": 159, "Van Horn": 522, "Victoria": 352, "Waco": 151, "Wichita Falls": 84, "Yoakum": 324}

Galveston_r = {"Houston": 50, "Huntsville": 119, "Junction": 340, "Kingsville": 254, "Laredo": 341, "Longview": 253, "Lubbock": 560, "Lufkin": 166, "McAllen": 367, "Odessa": 538, "Orange": 98, "Ozona": 430, "Paris": 342, "Pecos": 589, "San Angelo": 407, "San Antonio": 241, "South Padre Is": 387, "Temple": 217, "Texarkana": 328, "Tyler": 247, "Van Horn": 654, "Victoria": 154, "Waco": 230, "Wichita Falls": 421, "Yoakum": 157}

Houston_r = {"Huntsville": 69, "Junction": 296, "Kingsville": 232, "Laredo": 311, "Longview": 206, "Lubbock": 510, "Lufkin": 119, "McAllen": 345, "Odessa": 494, "Orange": 108, "Ozona": 386, "Paris": 291, "Pecos": 545, "San Angelo": 363, "San Antonio": 197, "South Padre Is": 366, "Temple": 167, "Texarkana": 283, "Tyler": 197, "Van Horn": 610, "Victoria": 124, "Waco": 180, "Wichita Falls": 371, "Yoakum": 118}

Huntsville_r = {"Junction": 291, "Kingsville": 295, "Laredo": 365, "Longview": 151, "Lubbock": 466, "Lufkin": 72, "McAllen": 398, "Odessa": 458, "Orange": 136, "Ozona": 379, "Paris": 224, "Pecos": 528, "San Angelo": 327, "San Antonio": 217, "South Padre Is": 428, "Temple": 126, "Texarkana": 235, "Tyler": 130, "Van Horn": 594, "Victoria": 186, "Waco": 130, "Wichita Falls": 303, "Yoakum": 158}

Junction_r = {"Kingsville": 267, "Laredo": 230, "Longview": 374, "Lubbock": 269, "Lufkin": 346, "McAllen": 349, "Odessa": 224, "Orange": 400, "Ozona": 91, "Paris": 364, "Pecos": 250, "San Angelo": 96, "San Antonio": 114, "South Padre Is": 400, "Temple": 178, "Texarkana": 442, "Tyler": 338, "Van Horn": 315, "Victoria": 227, "Waco": 211, "Wichita Falls": 276, "Yoakum": 198}

Kingsville_r = {"Laredo": 118, "Longview": 437, "Lubbock": 536, "Lufkin": 350, "McAllen": 113, "Odessa": 490, "Orange": 339, "Ozona": 357, "Paris": 496, "Pecos": 498, "San Angelo": 362, "San Antonio": 153, "South Padre Is": 133, "Temple": 272, "Texarkana": 515, "Tyler": 406, "Van Horn": 563, "Victoria": 111, "Waco": 308, "Wichita Falls": 488, "Yoakum": 141}

Laredo_r = {"Longview": 488, "Lubbock": 498, "Lufkin": 429, "McAllen": 143, "Odessa": 422, "Orange": 418, "Ozona": 289, "Paris": 527, "Pecos": 417, "San Angelo": 321, "San Antonio": 154, "South Padre Is": 216, "Temple": 299, "Texarkana": 572, "Tyler": 456, "Van Horn": 483, "Victoria": 187, "Waco": 334, "Wichita Falls": 490, "Yoakum": 208}

Longview_r = {"Lubbock": 447, "Lufkin": 87, "McAllen": 541, "Odessa": 472, "Orange": 195, "Ozona": 456, "Paris": 102, "Pecos": 546, "San Angelo": 372, "San Antonio": 334, "South Padre Is": 570, "Temple": 198, "Texarkana": 88, "Tyler": 36, "Van Horn": 633, "Victoria": 328, "Waco": 163, "Wichita Falls": 257, "Yoakum": 300}

Lubbock_r = {"Lufkin": 490, "McAllen": 618, "Odessa": 137, "Orange": 596, "Ozona": 218, "Paris": 383, "Pecos": 203, "San Angelo": 183, "San Antonio": 382, "South Padre Is": 668, "Temple": 343, "Texarkana": 475, "Tyler": 419, "Van Horn": 291, "Victoria": 489, "Waco": 345, "Wichita Falls": 208, "Yoakum": 457}

Lufkin_r = {"McAllen": 463, "Odessa": 491, "Orange": 120, "Ozona": 431, "Paris": 184, "Pecos": 565, "San Angelo": 360, "San Antonio": 285, "South Padre Is": 484, "Temple": 168, "Texarkana": 165, "Tyler": 84, "Van Horn": 642, "Victoria": 242, "Waco": 157, "Wichita Falls": 304, "Yoakum": 230}

McAllen_r = {"Odessa": 565, "Orange": 451, "Ozona": 432, "Paris": 594, "Pecos": 560, "San Angelo": 444, "San Antonio": 236, "South Padre Is": 73, "Temple": 366, "Texarkana": 624, "Tyler": 508, "Van Horn": 626, "Victoria": 220, "Waco": 401, "Wichita Falls": 572, "Yoakum": 241}

Odessa_r = {"Orange": 589, "Ozona": 133, "Paris": 447, "Pecos": 74, "San Angelo": 131, "San Antonio": 336, "South Padre Is": 622, "Temple": 336, "Texarkana": 525, "Tyler": 444, "Van Horn": 161, "Victoria": 447, "Waco": 340, "Wichita Falls": 293, "Yoakum": 413}

Orange_r = {"Ozona": 490, "Paris": 297, "Pecos": 649, "San Angelo": 458, "San Antonio": 303, "South Padre Is": 472, "Temple": 253, "Texarkana": 254, "Tyler": 204, "Van Horn": 714, "Victoria": 231, "Waco": 265, "Wichita Falls": 424, "Yoakum": 226}

Ozona_r = {"Paris": 434, "Pecos": 159, "San Angelo": 82, "San Antonio": 204, "South Padre Is": 490, "Temple": 263, "Texarkana": 512, "Tyler": 410, "Van Horn": 225, "Victoria": 318, "Waco": 282, "Wichita Falls": 311, "Yoakum": 289}

Paris_r = {"Pecos": 521, "San Angelo": 352, "San Antonio": 373, "South Padre Is": 629, "Temple": 228, "Texarkana": 92, "Tyler": 101, "Van Horn": 608, "Victoria": 385, "Waco": 194, "Wichita Falls": 178, "Yoakum": 358}

Pecos_r = {"San Angelo": 205, "San Antonio": 363, "South Padre Is": 630, "Temple": 410, "Texarkana": 599, "Tyler": 517, "Van Horn": 88, "Victoria": 476, "Waco": 413, "Wichita Falls": 366, "Yoakum": 448}

San_Angelo_r = {"San Antonio": 209, "South Padre Is": 495, "Temple": 205, "Texarkana": 430, "Tyler": 336, "Van Horn": 282, "Victoria": 316, "Waco": 209, "Wichita Falls": 230, "Yoakum": 282}

San_Antonio_r = {"South Padre Is": 286, "Temple": 146, "Texarkana": 418, "Tyler": 302, "Van Horn": 428, "Victoria": 114, "Waco": 181, "Wichita Falls": 336, "Yoakum": 94}

South_Padre_Is_r = {"Temple": 406, "Texarkana": 648, "Tyler": 540, "Van Horn": 696, "Victoria": 244, "Waco": 441, "Wichita Falls": 621, "Yoakum": 273}

Temple_r = {"Texarkana": 278, "Tyler": 162, "Van Horn": 476, "Victoria": 178, "Waco": 36, "Wichita Falls": 230, "Yoakum": 141}

Texarkana_r = {"Tyler": 116, "Van Horn": 686, "Victoria": 407, "Waco": 244, "Wichita Falls": 270, "Yoakum": 383}

Tyler_r = {"Van Horn": 605, "Victoria": 296, "Waco": 128, "Wichita Falls": 232, "Yoakum": 268}

Van_Horn_r = {"Victoria": 542, "Waco": 490, "Wichita Falls": 454, "Yoakum": 513}

Victoria_r = {"Waco": 202, "Wichita Falls": 399, "Yoakum": 39}

Waco_r = {"Wichita Falls": 198, "Yoakum": 172}

Wichita_Falls_r = {"Yoakum": 370}


cities = ["Abilene", "Amarillo", "Austin", "Beaumont", "Big Bend", "Big Spring", "Brownsville", "Brownwood", "Bryan", "Childress", "Corpus Christi", "Dalhart", "Dallas", "Del Rio", "Denison", "Eagle Pass", "El Paso", "Fort Stockton", "Fort Worth", "Gainsville", "Galveston", "Houston", "Huntsville", "Junction", "Laredo", "Longview", "Lubbock", "Lufkin", "McAllen", "Odessa", "Orange", "Ozona", "Paris", "Pecos", "San Angelo", "San Antonio", "South Padre Is", "Temple", "Texarkana", "Tyler", "Van Horn", "Victoria", "Waco", "Wichita Falls"]

d_city = {"Abilene": Abilene_r, "Amarillo": Amarillo_r, "Austin": Austin_r, "Beaumont": Beaumont_r, "Big Bend": Big_Bend_r, "Big Spring": Big_Spring_r, "Brownsville": Brownsville_r, "Brownwood": Brownwood_r, "Bryan": Bryan_r, "Childress": Childress_r, "Corpus Christi": Corpus_Christi_r, "Dalhart": Dalhart_r, "Dallas": Dallas_r, "Del Rio": Del_Rio_r, "Denison": Denison_r, "Eagle Pass": Eagle_Pass_r, "El Paso": El_Paso_r, "Fort Stockton": Fort_Stockton_r, "Fort Worth": Fort_Worth_r, "Gainsville": Gainsville_r, "Galveston": Galveston_r, "Houston": Houston_r, "Huntsville": Huntsville_r, "Junction": Junction_r, "Laredo": Laredo_r, "Longview": Longview_r, "Lubbock": Lubbock_r, "Lufkin": Lufkin_r, "McAllen": McAllen_r, "Odessa": Odessa_r, "Orange": Orange_r, "Ozona": Ozona_r, "Paris": Paris_r, "Pecos": Pecos_r, "San Angelo": San_Angelo_r, "San Antonio": San_Antonio_r, "South Padre Is": South_Padre_Is_r, "Temple": Temple_r, "Texarkana": Texarkana_r, "Tyler": Tyler_r, "Van Horn": Van_Horn_r, "Victoria": Victoria_r, "Waco": Waco_r, "Wichita Falls": Wichita_Falls_r}

start = "Abilene"
city1 = "Abilene"
#cities.remove("Abilene")
total_distance = 0

while len(cities) > 0:
    if city1 in cities:
        cities.remove(city1)

    the_distance = 10000
    closest_city = ""
    for city in cities:
        #print(city, '\t', city1, 'yo')
        if city < city1:
            a_distance = d_city[city][city1]
        else:
            a_distance = d_city[city1][city]

        if a_distance < the_distance:
            the_distance = a_distance
            closest_city = city

    print(city1, '\t', closest_city, '\t', the_distance)
    total_distance += the_distance
    print(f"\tTotal distance = {total_distance}")

    city1 = closest_city
    cities.remove(closest_city)

if city1 < start:
    a_distance = d_city[city1][start]
else:
    a_distance = d_city[start][city1]
print(city1, '\t', start, '\t', a_distance)
total_distance += the_distance
print(f"\tTotal distance = {total_distance}")


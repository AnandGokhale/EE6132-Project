"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
    'kitti2idd_train': 1334
}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
    'kitti2idd_train': '.png'
}

"""The path to the output csv file."""
PATH_TO_CSV = {
    'kitti2idd_train': './kitti2idd_train.csv'
}

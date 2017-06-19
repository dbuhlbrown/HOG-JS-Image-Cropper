import unittest
from crop_images import ImageCropper


class CropImagesTestCase(unittest.TestCase):

    def test_image_cropper_init_default_values(self):

        crop_images_test = ImageCropper()

        self.assertTrue( crop_images_test.positive_images_file == "" )
        self.assertTrue( crop_images_test.positive_cropped_directory == "" )
        self.assertTrue( crop_images_test.negative_cropped_directory == "" )
        self.assertTrue( crop_images_test.negative_images_directory == "" )
        self.assertTrue( crop_images_test.bounding_box_file == "" )
        self.assertTrue( crop_images_test.width == 0 )
        self.assertTrue( crop_images_test.height == 0 )
        self.assertTrue( crop_images_test.negative_row_buffer == -1)
        self.assertTrue( crop_images_test.negative_column_buffer == -1)

    def test_read_correct_config_file(self):

        crop_images_test = ImageCropper()
        crop_images_test.read_config_file("test_correct_config.json")

        self.assertTrue( crop_images_test.positive_images_file == "positive.txt" )
        self.assertTrue( crop_images_test.positive_cropped_directory == "positive_images/cropped_images/" )
        self.assertTrue( crop_images_test.negative_cropped_directory == "negative_images/cropped_images/" )
        self.assertTrue( crop_images_test.negative_images_directory == "negative_images/" )
        self.assertTrue( crop_images_test.bounding_box_file == "results.txt" )
        self.assertTrue( crop_images_test.width == 64 )
        self.assertTrue( crop_images_test.height == 64 )
        self.assertTrue( crop_images_test.negative_row_buffer == 7)
        self.assertTrue( crop_images_test.negative_column_buffer == 7)

    def test_compute_negative_buffers_sets_to_zero_correctly(self):

        crop_images_test = ImageCropper()
        crop_images_test.negative_column_buffer = 4
        crop_images_test.negative_row_buffer = 4

        neg_col_buffer, neg_row_buffer = crop_images_test.compute_negative_buffers(3,3)
        self.assertTrue( neg_col_buffer == 0 and neg_row_buffer == 0)

    def test_compute_negative_buffers_sets_to_zero_correctly_when_even(self):

        crop_images_test = ImageCropper()
        crop_images_test.negative_column_buffer = 4
        crop_images_test.negative_row_buffer = 4

        neg_col_buffer, neg_row_buffer = crop_images_test.compute_negative_buffers(4,4)
        self.assertTrue( neg_col_buffer == 0 and neg_row_buffer == 0)

    def test_compute_negative_buffers_are_4(self):

        crop_images_test = ImageCropper()
        crop_images_test.negative_column_buffer = 4
        crop_images_test.negative_row_buffer = 4

        neg_col_buffer, neg_row_buffer = crop_images_test.compute_negative_buffers(7,7)
        self.assertTrue( neg_col_buffer == 4 and neg_row_buffer == 4)

if __name__ == '__main__':
    unittest.main()

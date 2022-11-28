
# - Google Image Downloader : create a python function that takes a url of an
# image from google and save location , then download the image in the save
# location

# from bing_image_downloader import downloader


# def google_images():
#     strings_searsh = "dress,laptop,kids"
#     downloader.download(strings_searsh, limit=30,  output_dir='F:\\Download\\photos',
#                         adult_filter_off=True, force_replace=False, timeout=60, verbose=True)


# downlad = google_images()


from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"pussy,naked,sexy","limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images


# another functions to download image from google
'''from bing_image_downloader import downloader


def google_images():
    strings_search = "dress,laptop,kids"
    downloader.download(strings_search, limit=30,  output_dir='F:\\Download\\photos',
                        adult_filter_off=True, force_replace=False, timeout=60, verbose=True)


downland = google_images()'''
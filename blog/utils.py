


def post_image_path(instance, filename):
    return 'post-images/%s.%s' %(instance.title, filename.split(".")[-1]) 


Accepted = 1
Rejected = 2
Pending = 3
STATUS_TYPE =[
    (Accepted, 'در حال انتشار'),
    (Rejected, 'عدم تایید'),
    (Pending, 'پیش نویس'),
]

Scientific = 1
Educational = 2
News = 3
CATEGORY_TYPE =[
    (Scientific, 'علمی'),
    (Educational, 'آموزشی'),
    (News, 'خبری'),
]


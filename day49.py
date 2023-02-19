# pytorch for classification purposes CIFAR-10
from torchvision import datasets
import matplotlib.pyplot as plt
from torchvision import transforms

data_path = '../datasets/cifar10/'
# it is initialized a dataset for training purposes
cifar10 = datasets.CIFAR10(data_path, train = True, download = True)
# with train = False, the following gives a dataset for validation
# purposes
cifar10_val = datasets.CIFAR10(data_path, train = False, download = True)
# the Dataset object of PyTorch requires the implementation of
# @__len__@ and @__getitem__@
# when a python object is provided by a @__len__@ method,
# we can pass an object directly to the method
print(len(cifar10))
# in cifar10 there are 50000 elements

img, label = cifar10[10]#deer
print(label)

plt.imshow(img)
plt.show()

# to use images and data for deep learning, they have to be tensors
# we can rename the function to transform PIL objects and NumPy ones into tensors
to_tensor = transforms.ToTensor()
image_t = to_tensor(img)
print('Shape of the image_t: ', image_t.shape)

# the function for downloading and managing the datasets
# can be set to transform directly the PIL images to tensors
tensor_cifar10 = datasets.CIFAR10(data_path, train=True, download=False,
                                  transform=transforms.ToTensor())
img_t, label_t = tensor_cifar10[10]
# it is possible to see that the images are tensors
type(img_t)
print(img_t.shape)


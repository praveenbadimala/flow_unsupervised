import os.path
import glob
from .listdataset import ListDataset
from .util import split2list

# source ref: https://github.com/ClementPinard/FlowNetPytorch

def make_dataset(dir,split=None):
    '''Will search for triplets that go by the pattern '[name]_img1.ppm  [name]_img2.ppm    [name]_flow.flo' '''
    images = []
    for flow_map in glob.iglob(os.path.join(dir,'*_flow.flo')):
        flow_map = os.path.basename(flow_map)
        root_filename = flow_map[:-9]
        img1 = root_filename+'_img1.ppm'
        img2 = root_filename+'_img2.ppm'
        if not (os.path.isfile(os.path.join(dir,img1)) or os.path.isfile(os.path.join(dir,img2))):
            continue

        images.append([[img1,img2],flow_map])

    return split2list(images, split, default_split=0.97)

def get_file_triplets(dir):
    '''Will search for triplets that go by the pattern '[name]_img1.ppm  [name]_img2.ppm    [name]_flow.flo' '''
    images = []
    for flow_map in glob.iglob(os.path.join(dir,'*_flow.flo')):
        flow_map = os.path.basename(flow_map)
        root_filename = flow_map[:-9]
        img1 = root_filename+'_img1.ppm'
        img2 = root_filename+'_img2.ppm'
        if not (os.path.isfile(os.path.join(dir,img1)) or os.path.isfile(os.path.join(dir,img2))):
            continue

        images.append([[img1,img2],flow_map])
    return images


def flying_chairs(root, transform=None, target_transform=None,
                  co_transform=None, split=None):
    train_list, test_list = make_dataset(root,split)
    train_dataset = ListDataset(root, train_list, transform, target_transform, co_transform)
    test_dataset = ListDataset(root, test_list, transform, target_transform)

    return train_dataset, test_dataset
''' Samaneh Nobakht UCI:10059083
This script Segments the brain and head based on hipocampus masks for preparing binary masks for 3Dvisualisation in VR
'''
import vtk

# Load masks of both hippocampi, head with skull and brain
HipoLeft=vtk.vtkNIFTIImageReader()
HipoLeft.SetFileName("head_bet_left_Hipocampus_Resample.nii")
HipoLeft.Update()

HipoRight=vtk.vtkNIFTIImageReader()
HipoRight.SetFileName("head_bet_Right_Hipocampus_Resample.nii")
HipoRight.Update()
#Load original image
Head=vtk.vtkNIFTIImageReader()
Head.SetFileName("head.nii")
Head.Update()
#Load skull stripped mask
Brain=vtk.vtkNIFTIImageReader()
Brain.SetFileName("head_bet.nii")
Brain.Update()
BrainMask=vtk.vtkImageData()
BrainMask.DeepCopy(Brain.GetOutput())
#Smooth the original image
smooth= vtk.vtkImageMedian3D()
smooth.SetInputConnection(Head.GetOutputPort())
smooth.SetKernelSize(3,3,3)
smooth.Update()
Salt=smooth.GetOutput()
HeadMask=vtk.vtkImageData()
HeadMask.DeepCopy(Salt)
#................................................................................
'''Segment the whole head in head.nii image and call it HeadMask then emty the headmask by using skullstripped brain and then empty
skullstripped brain regions that belong to both hippocampi'''
for z  in range(0, Salt.GetDimensions()[2]):
  for y   in range(0,  Salt.GetDimensions()[1]):
    for x  in range (0,  Salt.GetDimensions()[0]):

        voxelValueSalt = Salt.GetScalarComponentAsFloat(x,y,z,0)
        if 70<voxelValueSalt<1000:
          HeadMask.SetScalarComponentFromFloat(x,y,z,0,1)
        else:
          HeadMask.SetScalarComponentFromFloat(x,y,z,0,0)
          voxelValueBrain = Brain.GetOutput().GetScalarComponentAsFloat(x,y,z,0)
        if 0.04<voxelValueBrain:
          BrainMask.SetScalarComponentFromFloat(x,y,z,0,1)
        else:
          BrainMask.SetScalarComponentFromFloat(x,y,z,0,0)
          voxelValueBrainMask = BrainMask.GetScalarComponentAsFloat(x,y,z,0)
        if voxelValueBrainMask==1:
          HeadMask.SetScalarComponentFromFloat(x,y,z,0,0)
          voxelValueHipoLeft = HipoLeft.GetOutput().GetScalarComponentAsFloat(x,y,z,0)
          voxelValueHipoRight = HipoRight.GetOutput().GetScalarComponentAsFloat(x,y,z,0)
        if voxelValueHipoLeft!=0 or voxelValueHipoRight!=0:
          BrainMask.SetScalarComponentFromFloat(x,y,z,0,0)
#............................................................................................
#Write resulting masks
writer1=vtk.vtkNIFTIImageWriter()
writer1.SetInputData(HeadMask)
writer1.SetFileName("HeadMask.nii")
writer1.Write()
writer2=vtk.vtkNIFTIImageWriter()
writer2.SetInputData(BrainMask)
writer2.SetFileName("BrainMask.nii")
writer2.Write()
#Define a function that takes an image and returns a same structured image but with zero values everywhere
def ZeroImage (image ):
    image1=vtk.vtkImageData()
    image1.DeepCopy(image)
    for z   in range(0,  image.GetDimensions()[2]):
     for y   in range(0,  image.GetDimensions()[1]):
       for x  in range (0,  image.GetDimensions()[0]):
        image1.SetScalarComponentFromFloat(x,y,z,0,0)
    return(image1)
#Define four  zero images of the same structure as HeadMask and BrainMask and call them Head1, Head2, Brain1, Brain2
Brain2=Brain1=ZeroImage(BrainMask)
Head2=Head1=ZeroImage(HeadMask)
'''Divide BrainMask  to two pieces from top to hippocampi level and from Hippocampi to cerebelum
and Divide HeadMask  to two pieces from top to hippocampi level and from Hippocampi to patient chin'''
for z   in range(0, 137):
  for y   in range(0,  BrainMask.GetDimensions()[1]):
    for x  in range (0,  BrainMask.GetDimensions()[0]):
     voxHead1=Mask.GetScalarComponentAsFloat(x,y,z,0)
     if voxHead1==1:
          Head1.SetScalarComponentFromFloat(x,y,z,0,1)

for z   in range(0, 137):
  for y   in range(0,  BrainMask.GetDimensions()[1]):
    for x  in range (0,  BrainMask.GetDimensions()[0]):
     voxBrain1=BrainMask.GetScalarComponentAsFloat(x,y,z,0)
     if voxBrain1==1:
          Brain1.SetScalarComponentFromFloat(x,y,z,0,1)

for z   in range(137,BrainMask.GetDimensions()[2]):
  for y   in range(0,  BrainMask.GetDimensions()[1]):
    for x  in range (0,  BrainMask.GetDimensions()[0]):
     voxHead2=HeadMask.GetScalarComponentAsFloat(x,y,z,0)
     if voxHead2==1:
           Head2.SetScalarComponentFromFloat(x,y,z,0,1)

for z   in range(137,BrainMask.GetDimensions()[2]):
  for y   in range(0,  BrainMask.GetDimensions()[1]):
    for x  in range (0,  BrainMask.GetDimensions()[0]):
     voxBrain2=BrainMask.GetScalarComponentAsFloat(x,y,z,0)
     if voxBrain2==1:
           Brain2.SetScalarComponentFromFloat(x,y,z,0,1)
#Write resulting images to prepare for marching cube application
writer3=vtk.vtkNIFTIImageWriter()
writer3.SetInputData(Brain2)
writer3.SetFileName("Brain2.nii")
writer3.Write()
writer4=vtk.vtkNIFTIImageWriter()
writer4.SetInputData(Head2)
writer4.SetFileName("Head2.nii")
writer4.Write()
writer5=vtk.vtkNIFTIImageWriter()
writer5.SetInputData(Head1)
writer5.SetFileName("Head1.nii")
writer5.Write()
writer6=vtk.vtkNIFTIImageWriter()
writer6.SetInputData(Brain1)
writer6.SetFileName("Brain1.nii")
writer6.Write()

''' Samaneh Nobakht UCI:10059083
This scripts produces 6 separate meshes of Upper brain, lower brain, upper head, lower head and left and right hippocampi to export to VR'''
import vtk
#Define renderer
renderer = vtk.vtkRenderer()
#Read upper head mask
reader1=vtk.vtkNIFTIImageReader()
reader1.SetFileName("Head1.nii")
reader1.Update()
#Create mesh of the upper head up to level of hippocampi
isoSurf1 = vtk.vtkMarchingCubes()
isoSurf1.SetInputData(reader1.GetOutput())
isoSurf1.SetValue(0,1)
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(isoSurf1.GetOutputPort())
mapper1.ScalarVisibilityOff()
#Create property for actor
prop1 = vtk.vtkProperty()
prop1.SetColor(1.0,0.0,0.0)
prop1.SetOpacity(0.6)
#Create actor and set mapper and property
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.SetProperty(prop1)
#Add actor to renderer
renderer.AddActor(actor1)
#...................
#Load mask of lower head from hippocampus to chin
reader2=vtk.vtkNIFTIImageReader()
reader2.SetFileName("Head2.nii")
reader2.Update()
#Mesh lower head
isoSurf2 = vtk.vtkMarchingCubes()
isoSurf2.SetInputData(reader2.GetOutput())
isoSurf2.SetValue(0,1)
mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(isoSurf2.GetOutputPort())
mapper2.ScalarVisibilityOff()
#Create property for actor
prop2 = vtk.vtkProperty()
prop2.SetColor(1.0,0.0,0.0)
prop2.SetOpacity(0.6)
#Create actor and set mapper and property
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.SetProperty(prop2)
#Create rendere and add actor
renderer.AddActor(actor2)
#...................
#Load upper brain mask from top till hippocampi level
reader3=vtk.vtkNIFTIImageReader()
reader3.SetFileName("Brain1.nii")
reader3.Update()
#Mesh upper brain
isoSurf3 = vtk.vtkMarchingCubes()
isoSurf3.SetInputData(reader3.GetOutput())
isoSurf3.SetValue(0,1)
mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputConnection(isoSurf3.GetOutputPort())
mapper3.ScalarVisibilityOff()
#Create property for actor
prop3 = vtk.vtkProperty()
prop3.SetColor(1.0,1.0,0.0)
prop3.SetOpacity(0.6)
#Create actor and set mapper and property
actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor3.SetProperty(prop3)
#Create rendere and add actor
renderer.AddActor(actor3)
#..................
#Create lower brain from hippocampi till cerebelum
reader4=vtk.vtkNIFTIImageReader()
reader4.SetFileName("Brain2.nii")
reader4.Update()
#Mesh lower brain
isoSurf4 = vtk.vtkMarchingCubes()
isoSurf4.SetInputData(reader4.GetOutput())
isoSurf4.SetValue(0,1)
mapper4 = vtk.vtkPolyDataMapper()
mapper4.SetInputConnection(isoSurf4.GetOutputPort())
mapper4.ScalarVisibilityOff()
#Create property for actor
prop4 = vtk.vtkProperty()
prop4.SetColor(1.0,1.0,0.0)
prop4.SetOpacity(0.6)
#Create actor and set mapper and property
actor4 = vtk.vtkActor()
actor4.SetMapper(mapper4)
actor4.SetProperty(prop4)
#Create rendere and add actor
renderer.AddActor(actor4)
#.....................
#Load mask of left hippocampus and mesh it
reader5=vtk.vtkNIFTIImageReader()
reader5.SetFileName("head_bet_left_Hipocampus_Resample.nii")
reader5.Update()
isoSurf5 = vtk.vtkMarchingCubes()
isoSurf5.SetInputData(reader5.GetOutput())
isoSurf5.SetValue(0,1)
mapper5 = vtk.vtkPolyDataMapper()
mapper5.SetInputConnection(isoSurf5.GetOutputPort())
mapper5.ScalarVisibilityOff()
#Create property for actor
prop5 = vtk.vtkProperty()
prop5.SetColor(0.0,0.0,1.0)
prop5.SetOpacity(1.0)
#Create actor and set mapper and property
actor5 = vtk.vtkActor()
actor5.SetMapper(mapper5)
actor5.SetProperty(prop5)
#Create rendere and add actor
renderer.AddActor(actor5)
#..................
# load right hippocampus mask and mesh it
reader6=vtk.vtkNIFTIImageReader()
reader6.SetFileName("head_bet_Right_Hipocampus_Resample.nii")
reader6.Update()
isoSurf6 = vtk.vtkMarchingCubes()
isoSurf6.SetInputData(reader6.GetOutput())
isoSurf6.SetValue(0,1)
mapper6= vtk.vtkPolyDataMapper()
mapper6.SetInputConnection(isoSurf6.GetOutputPort())
mapper6.ScalarVisibilityOff()
#Create property for actor
prop6 = vtk.vtkProperty()
prop6.SetColor(0.0,0.0,1.0)
prop6.SetOpacity(1.0)
#Create actor and set mapper and property
actor6 = vtk.vtkActor()
actor6.SetMapper(mapper6)
actor6.SetProperty(prop6)
#Create rendere and add actor
renderer.AddActor(actor6)
#..............................
#Create window and set renderer
window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)
#Create interactor and pass to window
interactor = vtk.vtkRenderWindowInteractor()
window.SetInteractor(interactor)
window.Render()
#Export all meshes
obj = vtk.vtkOBJExporter()
obj.SetFilePrefix("headbrhipomesh")
obj.SetRenderWindow(window)
obj.Write()
#initialize and start interactor
interactor.Initialize()
interactor.Start()

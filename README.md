# Background-Foreground-separation-of-MRI-images-using-Anisotropic-Diffusion-Filtering-Thresholding

![Alt text](Picture2.png?raw=true "Segmented Image")

Background foreground separation is one of the classical problem in MR domain.
Magnetic Resonance Imaging (MRI) uses magnets to capture detailed images of soft tissue in the body.
MRIs help diagnose or monitor treatment for:
1. Tumors and cysts
2. Disease of the liver, bile ducts, gallbladder, and pancreas
3. Certain types of heart problems
4. Pelvic pain in women such as endometriosis
5. Diseases of the brain and spine

Due to radio frequency inhomogeneity (image intensity variation) segmentation is problematic, caused by inaccuracies in the
magnetic resonance scanner. Tissu outside the brain, such as skin,fat and bone segmentation algorithm faced difficulty.
Removeal of non-brain tissues are mandatory for successful automatic segmantation

# Types of MR images
Though ".dcm" is a common extension (and is defined in the DICOM), on physical interchange media with a DICOMDIR (like CD, DVD, BD, MOD), no file extension at all is used (due to the encoding of file references in the DICOMDIR), So expect to see, for example, "I001" rather than "I001.dcm", etc.

# Nonlinear anisotropic diffusion filters
It is a iterative, tunable filters introduced by Perona and Malik.Gerig et al http://www.coe.utah.edu/~cs7640/readings/PeronaMalik-PAMI-1990.pdf. used such filters to enhance MR images.
These filters smooth or enhance MR images and detect edges,they might also be used for RF correction and/or intracranial boundary detection in MR images.diffusion filters can be used to enhance and detect object edges within images.


# Pipe-line used
Used Nonlinear Anisotropic Diffusion Filtering follower by hysteresis thresholding to achieve the desired result.
Hysteresis thresholding has consistently been able to defeat absolute thresholding.For hysteresis thresholding 
all we need is High and Low thresholding value.
High thresholding value : mean of image after perform Nonlinear Anisotropic Diffusion Filtering
Low thresholding value  : std of image after perform Nonlinear Anisotropic Diffusion Filtering

# Prerequisites
1. Python3.2 or higher (https://www.python.org/downloads/)
2. SimpleITK ( http://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/ )
```
pip install SimpleITK 
```
# installation and running
1. clone the repository
2. run HeadMaskGenerator.py inputimage folder: sample_mri_image(DICOM) and outputimage: OutputImg (png format)
3. or run M_mark1.py Input_Folder Output_Folder as a 2 argument in command line

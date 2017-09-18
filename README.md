# Background-Foreground-separation-of-MRI-images

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


# Nonlinear anisotropic diffusion filters
It is a iterative, tunable filters introduced by Perona and Malik.Gerig et al. used such filters to enhance MR images.
These filters smooth or enhance MR images and detect edges,they might also be used for RF correction and/or intracranial boundary detection in MR images.

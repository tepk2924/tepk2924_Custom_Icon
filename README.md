This is my custom icon for various programs
===========================================
# How to use
> 0. Install python libraries needed (numpy, pillow)
> 1. Execute "Convert_to_ICO.py"
> 2. When the script ask you "Input the image directory : ", copy-and-paste the directory of logo PNG files and enter.
> 3. .ico file will be generated.
> 4. (Optional) The .ico file may have some "partial alpha values" with the range of 1 to 254, which can cause some potential problem for some environment. To deal with that, execute "Remove_partial_alpha.py". When the script ask "Input the image directory : ", copy-and-paste the directory of the .ico file. New file with no partial alpha values will appear.
> 5. (Optional) If you want to verify whether the .ico file has some pixels with partial alpha values, execute "Check_alpha_values.py".
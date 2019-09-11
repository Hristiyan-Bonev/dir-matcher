# Installation

Add the following function to your ~/.bashrc or ~/.profile 
```
ccd(){
folder="$1"
script_path="PATH/TO/SCRIPT/cd.py"
if [ ! -z $folder ]
 then
   found_dir=$(python $script_path $folder)
   if [ ! -z $found_dir ]
     then
        cd $found_dir
     else
        echo "Folder $folder not found. Please try with better guess. :)"
   fi
 else
   echo "Please provide folder name"
fi
}
```


Make sure that you reload the ".bashrc" or ".profile" file, depending in which file you have added the function above.

`source ~/.bashrc` or `source ~/.profile`

# Usage

Now you can use newly created "ccd" command, just type `ccd <folder_name>` and see if it changes directory accordingly.
Keep in mind that the script will look for match into the directory from which you are executing ccd command.


# Note
#### Currently the threshold is set to 50%.
This threshold indicates that the provided folder name should have at least 50% match ratio with some folder in your current directory in order to do `cd` into it.
You can always decrease or increase this threshold, but keep in mind that this may lead to faulty results.

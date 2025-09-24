su
# echo "Installing Paru . . ."
# sudo pacman -S --needed base-devel
# git clone https://aur.archlinux.org/paru.git
# cd paru
# makepkg -si
# echo "Paru Installed."
# cd ..
# rm -rf paru
# echo "Removed Paru Directory."

applications_list=("zen-browser-bin" "steam" "kitty" "steam" "code" "vlc" "kate")

for item in "${applications_list[@]}"; do
    echo "Installing $item . . ."
    paru -S $item
    echo "$item  Installed."
done

# pip3 install --user -r requirements.txt
pip3 install --user uv
sudo apt update && sudo apt install -y --no-install-recommends pandoc texlive-latex-extra
set -e


SCHEME=${SCHEME:-"basic"}
PACKAGES=${PACKAGES:-""}
MIRROR=${MIRROR:-"https://mirror.ctan.org/systems/texlive/tlnet/"}

check_packages() {
	if ! dpkg -s "$@" >/dev/null 2>&1; then
		if [ "$(find /var/lib/apt/lists/* | wc -l)" = "0" ]; then
			echo "Running apt-get update..."
			apt-get update -y
		fi
		apt-get -y install --no-install-recommends "$@"
	fi
}

check_packages ca-certificates perl wget perl-modules libfontconfig1 fontconfig libfile-homedir-perl libyaml-tiny-perl

cd /tmp # working directory of your choice
wget "${MIRROR}/install-tl-unx.tar.gz" # or curl instead of wget
zcat < install-tl-unx.tar.gz | tar xf -
cd $(ls -d */ | grep install-tl-)
perl ./install-tl --no-interaction --scheme=$SCHEME --location $MIRROR

TEXLIVE_DIR=$(ls -d /usr/local/texlive/* | grep 20)
TEXLIVE_EXECUTABLES_DIR="$(ls -d $TEXLIVE_DIR/bin/*)"

# Install latex and latexmk
$TEXLIVE_EXECUTABLES_DIR/tlmgr install latex latex-bin latexmk

# Split $PACKAGES string into separate strings using comma as delimiter, trim the resulting strings after split, and install them
PACKAGES="xcolor etoolbox booktabs mdwtools fancyvrb beamer"
echo $PACKAGES | tr ',' '\n' | xargs -I % sh -c "$TEXLIVE_EXECUTABLES_DIR/tlmgr install %"


chmod -R 777 /usr/local/texlive/

ls $TEXLIVE_EXECUTABLES_DIR | xargs -I % ln -s $TEXLIVE_EXECUTABLES_DIR/% /usr/local/bin/%

# cleanup

rm -rf /var/lib/apt/lists/*
cd /tmp
rm -rf $(ls -d */ | grep install-tl-)
rm -rf install-tl-unx.tar.gz

echo "Done!"
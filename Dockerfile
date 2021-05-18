FROM ubuntu:20.04

ENV PATH $PATH:/usr/local/texlive/latest/bin/x86_64-linux

RUN \
    #
    # Install dependencies
    #
    apt update; \
    apt upgrade; \
    apt install perl wget -y; \
    #
    # Download texlive
    #
    cd tmp; \
    wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz; \
    tar xvf install-tl-unx.tar.gz; \
    rm -rf install-tl-unx.tar.gz; \
    ls | xargs -I {} mv {} install-tl; \
    cd install-tl; \
    #
    # Install texlive
    #
    echo "selected_scheme scheme-basic" >> ./texlive.profile; \
    ./install-tl -profile ./texlive.profile; \
    cd /usr/local/texlive; \
    mv ./$(ls | grep -E "[0-9]+") ./latest; \
    tlmgr update --self --all; \
    #
    # Clean cache
    #
    apt-get clean; \
    rm -rf /var/lib/apt/lists/*; \
    rm -rf /tmp/*;

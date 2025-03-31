FROM zhuhe0321/mpich-ubuntu
RUN apt install -y cmake

WORKDIR /app
RUN wget https://github.com/lammps/lammps/archive/refs/tags/patch_22Dec2022.tar.gz
RUN tar xzvf patch_22Dec2022.tar.gz
RUN cd lammps-patch_22Dec2022 && mkdir build && cd build && \
    cmake ../cmake/ -DPKG_MOLECULE=on -DPKG_KSPACE=on -DPKG_RIGID=on && make -j 4

CMD ["/bin/bash"]
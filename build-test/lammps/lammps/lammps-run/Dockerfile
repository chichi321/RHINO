FROM zhuhe0321/lammps as builder
WORKDIR /
COPY ldd.sh .
RUN bash ldd.sh lmp

FROM ubuntu:22.04
RUN apt update && apt install ash


COPY --from=builder /3rdParty/mpiexec/mpiexec.hydra   /usr/local/bin/mpirun
COPY --from=builder /3rdParty/mpiexec/hydra_pmi_proxy /usr/local/bin/hydra_pmi_proxy
COPY --from=builder /3rdParty/libs/                   /lib/

WORKDIR /app
COPY --from=builder /app/lammps-patch_22Dec2022/build/lmp  /app/mpi-func
COPY data.rhodo /app/
COPY in.rhodo /app/

ENV MPICH_PORT_RANGE "20000:20100"
CMD ["/bin/bash"]
# mpirun, -np, 2, ./mpi-func, -in, in.rhodo,  -var, x, 4, -var, y, 4, -var, z, 4

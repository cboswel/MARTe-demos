FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
ADD .bootstrap.sh /
RUN bash -c "/.bootstrap.sh"
RUN cd /MARTe-demos
RUN bash -c "/MARTe-demos/install/m2install.sh"
CMD /bin/bash

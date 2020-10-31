# Based on the official OpenMRS Reference Application image
FROM openmrs/openmrs-reference-application-distro:demo

# Download JProfiler library (change the Jprofiler version if needed)
RUN wget https://download-gcdn.ej-technologies.com/jprofiler/jprofiler_linux_11_1_4.tar.gz -P /tmp/ &&\
tar -xzf /tmp/jprofiler_linux_11_1_4.tar.gz -C /usr/local && \
rm /tmp/jprofiler_linux_11_1_4.tar.gz

# Setup the JProfiler agent path and expose the port for remote JProfiler connection
ENV JPAGENT_PATH="-agentpath:/usr/local/jprofiler11.1.4/bin/linux-x64/libjprofilerti.so=nowait"
EXPOSE 8849

# Overwriting the setenv.sh file in the base image (enabling JProfiler agent at the web server startup)
COPY setenv.sh /usr/local/tomcat/bin/

# Optional (already specified in the base image)
CMD ["/usr/local/tomcat/startup.sh"]
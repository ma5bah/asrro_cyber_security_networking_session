import subprocess


def run_ping(host):
    try:
        # Define the ping command as a list of arguments.
        # 'ping' is the command, '-c' specifies the number of pings (4 in this case),
        # and 'host' is the server or IP address we are trying to ping.
        command = ['ping', '-c', '4', host]  # '-c 4' sends 4 ping requests

        # Using subprocess.run() to execute the command. We use 'capture_output=True' to capture
        # both the standard output (stdout) and standard error (stderr), and 'text=True'
        # to get the output as a string instead of bytes.
        result = subprocess.run(command, capture_output=True, text=True)

        # Return the output from stdout and stderr. stdout contains the successful output of the ping command,
        # and stderr will capture any error messages (e.g., if the host cannot be reached).
        return (result.stdout, result.stderr)

    except Exception as e:
        return str(e), None

# You run the command ping google.com.
# Your device sends an ICMP Echo Request to Google's server.
# Google's server responds with an ICMP Echo Reply.
# Ping calculates how long the process took and whether all packets were successfully sent and received.

if __name__ == "__main__":
    # Define the host to ping
    host = 'google.com'

    # Run the ping command and get the output
    # tuple
    (output, error) = run_ping(host)

    # Print the results
    if error:
        print("Error:", error)
    else:
        print("Ping Output:")
        print(output)

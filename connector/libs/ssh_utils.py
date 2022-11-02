"""
    It process the output ssh data
"""
class ProcessDataFactory:
    __password = None

    def __init__(self, password) -> None:
        if ProcessDataFactory.__password is None:
            ProcessDataFactory.__password = password

    @classmethod
    def loop_output(cls, cmd_output, sudo=False):
        output = ''
        # passing password for sudo user to execute command
        if sudo is True and cls.__password:
            for hostout in cmd_output:
                hostout.stdin.write(f'{cls.__password}\n')
                hostout.stdin.flush()
        # it waits until all remote commands in output have finished
        # cls().__connector.join(cmd_output)

        # looping through generator(object) for each host output
        for host_out in cmd_output:
            if host_out.stderr:
                # concating the error output
                for err_line in host_out.stderr:
                    # print(err_line)
                    output += err_line + '\n'

            if host_out.stdout:
                # concating the cmd output
                for line in host_out.stdout:
                    # print(line)
                    output += line + '\n'

        return output

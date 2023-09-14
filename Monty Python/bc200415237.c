#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int pipefd[2];
    pid_t child_pid;
    char child_pid_str[10];

    if (pipe(pipefd) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    child_pid = fork();
    if (child_pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (child_pid == 0) {
        pid_t child_process_pid = getpid();
        sprintf(child_pid_str, "%d", child_process_pid);
        if (write(pipefd[1], child_pid_str, sizeof(child_pid_str)) == -1) {
            perror("write");
            exit(EXIT_FAILURE);
        }
        exit(EXIT_SUCCESS);
    } else {
        if (read(pipefd[0], child_pid_str, sizeof(child_pid_str)) == -1) {
            perror("read");
            exit(EXIT_FAILURE);
        }
        printf("Parent (pid=%d): Received child process ID %s\n", getpid(), child_pid_str);
        printf("Parent (pid=%d): Parent process ID is %d\n", getpid(), getpid());
    }

    return 0;
}


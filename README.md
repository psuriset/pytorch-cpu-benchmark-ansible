# PyTorch CPU Benchmark Ansible Repo

This repo installs PyTorch on target hosts, runs CPU benchmarks, saves logs on the remote host, and fetches results back to the control machine.

## Repo layout

```text
pytorch-cpu-benchmark-ansible/
├── ansible.cfg
├── inventory/
│   └── hosts.ini
├── playbooks/
│   └── run_pytorch_cpu_bench.yml
├── roles/
│   └── pytorch_cpu_bench/
│       ├── tasks/
│       │   └── main.yml
│       ├── templates/
│       │   └── cpu_bench.py.j2
│       └── files/
│           └── requirements.txt
└── results/
```

## 1. Edit inventory

```ini
[bench_nodes]
myhost ansible_host=192.168.1.50 ansible_user=cloud-user
```

For local testing:

```ini
[bench_nodes]
localhost ansible_connection=local
```

## 2. Run

```bash
ansible-playbook -i inventory/hosts.ini playbooks/run_pytorch_cpu_bench.yml
```

## 3. Override benchmark settings

```bash
ansible-playbook -i inventory/hosts.ini playbooks/run_pytorch_cpu_bench.yml \
  -e bench_threads="1,2,4,8,16" \
  -e matrix_size=4096 \
  -e min_run_time=5
```

## 4. Result files

Remote:

```text
/tmp/pytorch-cpu-bench/results/
```

Fetched locally:

```text
./results/<hostname>/
```

## Useful variables

| Variable | Default | Meaning |
|---|---:|---|
| `bench_dir` | `/tmp/pytorch-cpu-bench` | Remote benchmark directory |
| `venv_dir` | `/tmp/pytorch-cpu-bench/venv` | Python virtualenv path |
| `bench_threads` | `1,2,4,8` | Thread counts to test |
| `matrix_size` | `4096` | Matrix size for `x @ w` |
| `min_run_time` | `5` | Seconds per benchmark sample |
| `python_bin` | `python3` | Python executable |

## Example deeper run

```bash
ansible-playbook -i inventory/hosts.ini playbooks/run_pytorch_cpu_bench.yml \
  -e bench_threads="1,2,4,8,16,32,64" \
  -e matrix_size=8192 \
  -e min_run_time=10
```

# 16-Week Self-Directed Semester: C++ / OS / ML / RL / Isaac Sim

> 목표: 16주 동안 **Modern C++(3학점) + Operating Systems/Systems(3학점) + Machine Learning(3학점) + Reinforcement Learning(3학점) + Isaac Sim Robotics Project(6학점)**을 하나의 종속성 있는 커리큘럼으로 운영한다.  
> 핵심 원칙: 네 과목을 따로 끝내는 것이 아니라, **C++/OS/ML이 Isaac Sim 프로젝트에 필요한 능력을 앞서 공급하도록** 구성한다.

---

## 0. 전체 구조

### 학점 배분

| 과목 | 학점 | 주 역할 |
|---|---:|---|
| Modern C++ | 3 | C++ 문법, lifetime/ownership, STL, RAII, concurrency 기초 |
| Operating Systems & Systems Programming | 3 | process/thread, scheduling, virtual memory, synchronization, timing |
| Machine Learning / PyTorch | 3 | 확률적 관점, 고전 ML, PyTorch, 딥러닝 기초 |
| Reinforcement Learning | 3 | MDP, value/policy, policy gradient, PPO |
| Isaac Sim / Isaac Lab Robotics Project | 6 | robot modeling, control, disturbance, randomization, RL 적용, evaluation |

### 선수관계

```text
C++ 기초
 ├──────────────→ OS 실습
 │                    ↓
 │              threads / timing
 │                    ↓
 └──────────────→ 로봇 시스템 구현
                       ↑
확률/고전 ML → PyTorch / DL → RL → PPO
                                  ↑
Isaac Sim → PD → deterministic disturbance
                       ↓
                domain randomization
                       ↓
                Isaac RL 적용
```

### 운영 강도

이 커리큘럼은 **총 18학점 상당**으로 본다.

```text
Modern C++                     3
Operating Systems / Systems    3
Machine Learning               3
Reinforcement Learning         3
Isaac Sim Robotics Project     6
--------------------------------
Total                         18
```

단, 과목 간 중복 학습이 있으므로 체감 시간은 일반적인 18학점 전공학기와 비슷하거나 약간 낮을 수 있다.  
대신 Isaac 프로젝트 디버깅이 길어지는 주에는 주당 시간이 크게 늘 수 있다.

### 한 학기의 최종 결과물

16주 뒤에는 최소 다음이 Git 저장소에 남아 있어야 한다.

- C++ 실습 코드와 작은 프로젝트
- OS/system programming 실습
- PyTorch/ML 실습
- Isaac Sim custom robot/environment
- PD baseline controller
- deterministic disturbance benchmark
- domain randomization framework
- PPO/RL policy
- PD vs RL benchmark
- 최종 보고서
- 실험 그래프/영상
- 재현 가능한 README

---

# 1. 공부 자료

영상 자료는 사용하지 않는다.

---

## A. Modern C++ — 3학점

### 주교재

**LearnCpp**

https://www.learncpp.com/

가능하면 처음부터 순서대로 1회독한다. 이미 아는 문법은 빨리 지나가되 다음 항목은 천천히 본다.

- compilation / linking
- header/source separation
- references
- pointers
- const
- scope / lifetime
- classes
- constructors / destructors
- RAII
- copy / move semantics
- smart pointers
- STL containers
- iterators
- lambdas
- templates
- concurrency

### 보조자료

**cppreference**

https://en.cppreference.com/

교재처럼 정독하지 않는다.  
특정 표준 라이브러리 기능의 정확한 동작과 API를 확인하는 레퍼런스로 사용한다.

---

## B. Operating Systems & Systems Programming — 3학점

### 주교재: OSTEP

**Operating Systems: Three Easy Pieces — Remzi & Andrea Arpaci-Dusseau**

https://pages.cs.wisc.edu/~remzi/OSTEP/

무료로 전체 챕터가 공개되어 있고, CPU virtualization → memory virtualization → concurrency → persistence 순서로 읽을 수 있다.

이 커리큘럼에서는 특히 다음 챕터를 우선한다.

### 필수

- Introduction
- The Abstraction: The Process
- Process API
- Mechanism: Limited Direct Execution
- CPU Scheduling
- Multi-level Feedback Queue
- Multiprocessor Scheduling
- Address Spaces
- Memory API
- Address Translation
- Paging
- TLB
- Threads
- Thread API
- Locks
- Condition Variables
- Semaphores
- Concurrency Bugs

### 후순위

- file systems
- disks
- RAID
- distributed systems

로봇/실시간/임베디드 방향에서는 당장 concurrency와 scheduling이 더 중요하다.

### 실습 참고자료

Linux에서 다음 API를 직접 man page로 읽는다.

```bash
man fork
man execve
man wait
man pipe
man mmap
man pthread_create
man pthread_mutex_lock
man pthread_cond_wait
man sem_init
man clock_gettime
man clock_nanosleep
```

**Linux man-pages online**

https://man7.org/linux/man-pages/

시스템 프로그래밍에서는 블로그보다 man page를 우선한다.

---

## C. Machine Learning / PyTorch — 3학점

이 과목은 다음 순서로 진행한다.

```text
확률/통계적 관점
→ 고전 머신러닝
→ PyTorch
→ 딥러닝 기초
```

목표는 RL까지 한 과목에 억지로 넣는 것이 아니라, **회귀·분류·확률적 추정·일반화·최적화가 신경망으로 어떻게 이어지는지 이해하는 것**이다.

### 주교재

**Probabilistic Machine Learning: An Introduction — Kevin P. Murphy**

https://probml.github.io/pml-book/book1.html

전체를 정독하지 않는다. 다음 주제를 중심으로 선택적으로 읽는다.

- probability review
- common probability distributions
- maximum likelihood estimation
- Bayesian inference / MAP
- linear regression
- logistic regression
- generative vs discriminative models
- overfitting / regularization
- bias-variance tradeoff
- PCA
- kernel methods / SVM — 개념과 핵심 수식 위주

특히 다음 연결을 이해하는 것이 목표다.

```text
probability distribution
→ likelihood
→ loss function
→ optimization
→ prediction
```

### 보조교재

**An Introduction to Statistical Learning (ISLR)**

https://www.statlearning.com/

Murphy가 너무 수학적으로 느껴질 때 설명용으로 사용한다.

우선순위:

- Linear Regression
- Classification
- Resampling
- Regularization
- Support Vector Machines
- Tree-Based Methods — 개념 위주
- Unsupervised Learning / PCA

### PyTorch 공식 기본 과정

**PyTorch — Learn the Basics**

https://docs.pytorch.org/tutorials/beginner/basics/

읽을 순서:

1. Quickstart
2. Tensors
3. Datasets & DataLoaders
4. Transforms
5. Build the Neural Network
6. Automatic Differentiation
7. Optimization
8. Save / Load Model

한국어판:

https://tutorials.pytorch.kr/beginner/basics/

### Deep Learning

**Dive into Deep Learning (D2L)**

https://d2l.ai/

필요한 부분만 읽는다.

- linear regression 복습
- softmax regression
- multilayer perceptrons
- optimization
- convolutional neural networks
- recurrent neural networks — 개념 위주
- attention / transformers — 개념 위주

### 이 과목에서 반드시 가져갈 것

- 선형회귀
- 로지스틱 회귀
- MLE / MAP
- train / validation / test split
- overfitting
- regularization
- bias-variance
- PCA
- SVM과 margin의 개념
- kernel trick의 의미
- generative vs discriminative model
- PyTorch `Tensor`, `Dataset`, `DataLoader`, `nn.Module`
- autograd / optimizer / training loop
- MLP / CNN 기본 구조

### 가볍게 이해만 해도 되는 것

- decision tree / ensemble
- Gaussian mixture model / EM
- Gaussian process
- RNN / LSTM
- attention / Transformer

---

## D. Reinforcement Learning — 3학점

ML에서 분리하여 별도 과목으로 운영한다.

목표는 **MDP와 value/policy의 의미를 이해하고, policy gradient와 PPO를 Isaac Lab에 적용할 수 있는 수준까지 가는 것**이다.

### 주교재

**Reinforcement Learning: An Introduction — Sutton & Barto**

공식 저자 사이트:

http://incompleteideas.net/book/the-book-2nd.html

우선순위:

- Chapter 1: Introduction
- Chapter 3: Finite MDPs
- Chapter 4: Dynamic Programming — 개념 위주
- Chapter 5: Monte Carlo
- Chapter 6: Temporal-Difference Learning
- Chapter 9~10: Approximation 개념
- Chapter 13: Policy Gradient Methods

### PPO 참고자료

**OpenAI Spinning Up — PPO**

https://spinningup.openai.com/en/latest/algorithms/ppo.html

중점:

- state / action / reward
- return
- policy
- value function
- advantage
- actor / critic
- policy gradient
- importance ratio
- clipping
- entropy
- rollout → update cycle

### 이 과목의 목표

다음 흐름을 설명할 수 있어야 한다.

```text
environment interaction
→ rollout
→ return / advantage estimate
→ policy update
→ value update
→ new rollout
```

그리고 Isaac Lab의 PPO config를 읽었을 때 주요 항목의 역할을 대략 설명할 수 있어야 한다.

---

## E. Isaac Sim / Isaac Lab — 6학점

현재 기준 주력 버전은 **Isaac Sim 6.0.1 계열 공식 문서**를 사용한다.

### Isaac Sim 공식 문서

https://docs.isaacsim.omniverse.nvidia.com/latest/

### Robot Setup Tutorials

https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/index.html

우선순위:

1. Stage Setup
2. Assemble a Simple Robot
3. Articulate a Basic Robot
4. Add Camera and Sensors
5. Rig a Mobile Robot
6. Manipulator 관련 튜토리얼 — 필요할 때
7. Joint drive tuning
8. Asset optimization

### Articulation / Joint

https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_gui_simple_robot.html

중점:

- rigid body
- joint
- drive
- articulation root
- fixed-base / floating-base articulation
- position / velocity / effort command

### Robot Simulation / Controllers

https://docs.isaacsim.omniverse.nvidia.com/latest/robot_simulation/index.html

### Sensors

https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/index.html

특히:

- joint state
- IMU
- articulation joint force
- camera
- contact sensor

### Isaac Lab

https://isaac-sim.github.io/IsaacLab/

Isaac Sim 자체를 어느 정도 이해한 다음 사용한다.

### Isaac Lab Environment 구조

https://isaac-sim.github.io/IsaacLab/develop/source/tutorials/03_envs/create_manager_base_env.html

중점:

- Scene
- Observation
- Action
- Event
- Reset
- Reward
- Termination
- Curriculum

### Domain Randomization / Events

https://isaac-sim.github.io/IsaacLab/develop/source/api/lab/isaaclab.envs.mdp.html

여기서 다음 기능들을 찾아서 실험한다.

- external force / torque
- push
- mass randomization
- center-of-mass randomization
- friction randomization
- actuator gain randomization
- joint parameter randomization
- gravity randomization
- randomized reset

### RL in Isaac Lab

https://isaac-sim.github.io/IsaacLab/develop/source/concepts/reinforcement_learning.html

새 프로젝트에서는 특별한 이유가 없다면 **RSL-RL + PPO**를 우선 후보로 둔다.

---

# 2. 16주 커리큘럼

---

## Week 1 — 환경과 기본 실행 모델

### C++

- LearnCpp 시작
- program structure
- variables / initialization
- functions
- namespace
- compilation / linking
- source/header separation

### OS

OSTEP:

- Introduction
- Process

질문:

- program과 process의 차이는?
- CPU는 여러 process를 어떻게 동시에 실행하는 것처럼 보이게 하는가?

### ML

고전 ML / 확률적 기반 시작.

- 확률변수와 확률분포 복습
- expectation / variance
- likelihood
- maximum likelihood estimation
- train / validation / test의 역할

작은 NumPy 실습:

- Gaussian data 생성
- 평균/분산 추정
- likelihood 변화 관찰

아직 PyTorch는 본격적으로 사용하지 않는다.

### RL

아직 시작하지 않는다.

### Isaac

- USD / Prim / Xform
- Rigid Body
- Collider
- Physics Scene
- 간단한 scene 직접 제작

### 결과물

```text
week01/
├── cpp/
├── os/
├── ml/
└── isaac/
```

---

## Week 2 — Multi-file C++ / Process API / PyTorch workflow / Joint

### C++

- header
- forward declaration
- multiple translation units
- CMake 기본

### OS

OSTEP:

- Process API
- Limited Direct Execution

Linux:

```text
fork
exec
wait
```

직접 작은 실습 프로그램 작성.

### ML

고전 ML:

- linear regression
- least squares
- MSE
- regularization
- bias / variance

직접 NumPy로 선형회귀 구현.

가능하면 closed-form solution과 gradient descent를 둘 다 비교한다.

### RL

아직 시작하지 않는다.

### Isaac

- rigid bodies 연결
- revolute joint
- fixed joint
- joint drive
- articulation

### 목표

직접 만든 간단한 articulated mechanism이 정상적으로 움직인다.

---

## Week 3 — Pointer / Thread 개념 / Neural Network / Robot API

### C++

- references
- pointers
- arrays
- std::vector
- struct
- class

### OS

OSTEP:

- CPU Scheduling
- MLFQ

### ML

고전 ML:

- logistic regression
- sigmoid
- cross-entropy
- probabilistic classification
- MLE와 classification loss의 연결

직접 binary classifier 구현.

추가:

- generative vs discriminative model

### RL

아직 시작하지 않는다.

### Isaac

Python에서:

- articulation state 읽기
- joint position
- joint velocity
- target command 보내기

### 목표

```text
target
  ↓
controller/API
  ↓
joint
  ↓
sensor state
```

파이프라인 완성.

---

## Week 4 — Lifetime / Memory / Backprop / Robot baseline environment

### C++

- scope
- lifetime
- stack / heap 개념
- const
- reference/pointer 복습

### OS

OSTEP:

- Address Spaces
- Memory API
- Address Translation

Linux:

```text
malloc/new
mmap
```

### ML

고전 ML 마무리:

- regularization
- bias-variance tradeoff
- PCA
- SVM
- margin
- kernel trick

SVM은 직접 완전 구현할 필요는 없지만, 다음은 설명할 수 있어야 한다.

```text
왜 margin을 최대화하는가?
soft margin은 왜 필요한가?
kernel trick은 무엇을 우회하는가?
```

간단한 PCA 실습을 직접 한다.

### RL

아직 시작하지 않는다.

### Isaac

nominal environment 확정.

예:

```text
base
 └── yaw
      └── pitch
           └── payload
```

센서/actuator 인터페이스 고정.

---

## Week 5 — PD Baseline

### C++

- constructors
- destructors
- member initialization
- encapsulation

### OS

- timer
- clock
- periodic task 개념

Linux:

```text
clock_gettime
clock_nanosleep
```

### ML

이제 PyTorch 시작.

공식 Learn the Basics:

- Tensor
- Dataset
- DataLoader
- `nn.Module`
- loss
- optimizer

고전 ML에서 직접 구현했던 linear/logistic regression을 PyTorch로 다시 구현한다.

### RL

아직 시작하지 않는다.

### Isaac

PD controller 구현.

\[
\tau = K_p(q_d-q)+K_d(\dot q_d-\dot q)
\]

측정:

- rise time
- overshoot
- settling time
- steady-state error
- control effort

### 조건

**외란 없이 먼저 안정화되어야 한다.**

---

## Week 6 — Deterministic Disturbance

### C++

LearnCpp 계속 진행.

### OS

periodic control loop 구현.

측정:

- target frequency
- actual frequency
- jitter

### ML

PyTorch:

- autograd
- computational graph
- backward
- optimizer
- training loop

MLP를 직접 학습시키고 NumPy 구현과 비교한다.

### RL

아직 시작하지 않는다.

### Isaac

고정 외란 하나씩 추가.

예:

- fixed impulse
- fixed torque
- base rotation
- sinusoidal disturbance

아직 randomization은 하지 않는다.

### 이유

제어기가 실패했을 때 원인을 분리하기 위해서다.

---

## Week 7 — RAII / Virtual Memory / CNN

### C++

중요 주차.

- RAII
- copy constructor
- copy assignment
- move constructor
- move assignment
- unique_ptr
- shared_ptr

직접 객체 생성/복사/이동/소멸 로그 실험.

### OS

OSTEP:

- Paging
- TLB
- Advanced Page Tables

### ML

Deep Learning:

- MLP
- activation functions
- initialization
- optimization
- regularization
- CNN
- convolution
- pooling

FashionMNIST 또는 CIFAR-10.

### RL

시작.

Sutton & Barto:

- Chapter 1
- Chapter 3
- state / action / reward
- return
- policy
- value function

### Isaac

PD controller parameter sweep.

예:

```text
Kp × Kd grid
```

그래프 생성.

---

## Week 8 — Midterm Project

새 진도 최소화.

### 중간 프로젝트 요구사항

- custom robot/environment
- sensor
- actuator
- PD controller
- deterministic disturbance
- quantitative metrics
- plots

### 중간 보고서

약 5~10페이지.

구조:

```text
Problem
Environment
Robot Model
Controller
Disturbance
Metrics
Results
Discussion
```

### C++ 시험

- pointer/reference
- lifetime
- RAII
- copy/move

### OS 시험

- process/thread
- scheduling
- virtual memory

### ML 시험

- likelihood / MLE
- linear regression
- logistic regression
- regularization
- bias-variance
- PCA
- SVM / margin / kernel trick
- PyTorch tensor / `nn.Module` 기초

### RL 중간 점검

- state / action / reward
- return
- policy
- value function
- MDP

---

## Week 9 — Domain Randomization

### OS

OSTEP concurrency 시작:

- Threads
- Thread API

### ML

Deep Learning 확장:

- generalization
- regularization
- data augmentation
- sequence model 개요
- RNN / LSTM — 개념 위주
- attention / Transformer — 개념 위주

이 시점에서 ML 3학점의 핵심 내용은 거의 마무리한다.

### RL

- Bellman equation
- dynamic programming 개념
- Monte Carlo
- Temporal-Difference learning

### Isaac Lab

randomization framework 작성.

한꺼번에 넣지 않는다.

순서 예:

1. disturbance magnitude
2. disturbance direction
3. payload mass
4. center of mass
5. friction
6. sensor noise
7. actuator gain
8. delay

### 결과

PD robustness benchmark 생성.

---

## Week 10 — Concurrency / Value-based RL

### C++

- STL
- iterators
- algorithms
- lambdas

### OS

OSTEP:

- Locks
- Locked Data Structures

### ML

- PyTorch 복습
- 필요한 부분만 보충
- CNN 결과 정리

### RL

- TD learning
- value function approximation 개념
- exploration / exploitation
- on-policy vs off-policy 개념

### 실습

CartPole 같은 작은 환경으로 RL workflow를 이해한다.

Isaac에는 아직 RL을 붙이지 않는다.

---

## Week 11 — Synchronization / PPO

### C++

- templates
- generic programming 기초

### OS

OSTEP:

- Condition Variables
- Semaphores
- Concurrency Bugs

Linux 실습:

```text
pthread
mutex
condition variable
semaphore
```

### ML

필요한 PyTorch 기능 복습.

- model save/load
- batching
- device
- experiment logging 구조

### RL

policy gradient → PPO.

중점:

- policy gradient의 기본 아이디어
- actor / critic
- advantage
- importance ratio
- clipping
- entropy

```text
rollout
→ return / advantage
→ policy update
→ value update
→ rollout
```

### 목표

Isaac Lab의 PPO config를 읽었을 때 각 항목의 역할을 대략 설명할 수 있어야 한다.

---

## Week 12 — RL Nominal Environment

### C++

필요한 LearnCpp 미완료 부분 보충.

### OS

producer-consumer queue 구현.

### RL / Isaac

Isaac Lab + RSL-RL 연결.

Observation 예:

```text
joint position
joint velocity
base angular velocity
target orientation
```

Action 후보:

```text
torque
```

또는

```text
joint target
```

Reward 예:

```text
-orientation_error
-angular_velocity
-control_effort
```

### 중요

**randomization 없이 nominal environment에서 먼저 학습이 되는지 확인한다.**

---

## Week 13 — Randomized RL

### RL / Isaac

Week 9에서 만든 randomization을 RL training에 연결한다.

비교:

```text
RL nominal training
vs
RL randomized training
```

randomization은 단계적으로 증가.

예:

```text
Stage 1: disturbance
Stage 2: + payload
Stage 3: + noise
Stage 4: + actuator variation
```

---

## Week 14 — PD vs RL Benchmark

### RL / Isaac

동일한 테스트 조건에서 비교한다.

| Test | PD | RL Nominal | RL Randomized |
|---|---:|---:|---:|
| Nominal | | | |
| Small disturbance | | | |
| Large disturbance | | | |
| Payload variation | | | |
| Noise | | | |
| Actuator variation | | | |

Metric:

- orientation RMSE
- maximum deviation
- settling time
- failure rate
- control effort

RL이 반드시 PD보다 좋아야 하는 것은 아니다.

---

## Week 15 — Systems Integration

### C++ / OS 프로젝트

다음 구조의 multi-thread program 작성.

```text
Sensor Thread
      ↓
shared state / queue
      ↓
Control Thread
      ↓
Actuator

Logging Thread
```

예:

```text
Sensor   500 Hz
Control  200 Hz
Logger    20 Hz
```

사용:

- `std::thread`
- mutex
- condition_variable
- atomic
- queue

관찰:

- mutex contention
- blocking
- missed deadline
- jitter
- slow logging의 영향

### 추가 선택과제

간단한 MCU scheduler 설계 시작.

---

## Week 16 — Final

새 내용 공부 금지.

### 최종 실험

- PD nominal
- PD disturbance
- PD randomized test
- RL nominal
- RL randomized
- PD vs RL

### 최종 보고서

```text
1. Introduction
2. Problem Formulation
3. Simulation Environment
4. Robot / Dynamics
5. Baseline Controller
6. Disturbance Model
7. Domain Randomization
8. RL Method
9. Experimental Setup
10. Results
11. Discussion
12. Limitations
13. Future Work
```

### Git 저장소 마무리

```text
robotics-semester/
├── cpp/
│   ├── exercises/
│   └── concurrency/
├── os/
│   ├── process/
│   ├── memory/
│   └── synchronization/
├── ml/
│   ├── pytorch/
│   └── rl/
├── isaac/
│   ├── assets/
│   ├── envs/
│   ├── controllers/
│   ├── randomization/
│   └── rl/
├── experiments/
├── plots/
├── report/
├── CURRICULUM.md
└── README.md
```

---

# 3. 권장 주간 시간

15학점 상당으로 운영한다면 목표는 **주 30시간 전후**.

| 영역 | 1~4주 | 5~8주 | 9~12주 | 13~16주 |
|---|---:|---:|---:|---:|
| C++ | 6h | 5h | 4h | 3h |
| OS | 5h | 5h | 6h | 5h |
| ML | 7h | 7h | 4h | 3h |
| RL | 0h | 3h | 7h | 6h |
| Isaac | 10h | 10h | 11h | 14h |
| 합계 | 28h | 30h | 32h | 31h |

시간 자체보다 **산출물**을 우선한다.

---

# 4. 주간 운영 예시

```text
월: C++ + Isaac
화: ML + Isaac
수: C++ + OS
목: ML 또는 RL + Isaac
금: OS + RL
토: Isaac 프로젝트 / 실험 / 과제
일: 복습 / 주간 보고서 / 다음 주 계획
```

매일 네 과목을 모두 하지 않는다.

---

# 5. 매주 Git에 남길 것

매주 최소:

```text
weekXX/
├── notes.md
├── exercises/
├── experiment/
└── retrospective.md
```

`retrospective.md`에는 다음 네 질문에 답한다.

1. 이번 주에 무엇을 배웠는가?
2. 책 없이 직접 구현할 수 있는 것은 무엇인가?
3. 아직 설명하지 못하는 개념은 무엇인가?
4. 다음 주 프로젝트 진행을 막는 prerequisite는 무엇인가?

---

# 6. 평가 방식

대학 수업처럼 스스로 평가한다.

| 항목 | 비율 |
|---|---:|
| 주간 실습/과제 | 25% |
| 중간시험 | 10% |
| 중간 프로젝트 | 20% |
| 최종 프로젝트 | 35% |
| 문서화 / 재현성 | 10% |

### A

- 주요 개념을 설명 가능
- 코드를 직접 작성 가능
- 최종 실험 재현 가능
- README만 보고 다른 사람이 실행 가능

### B

- 튜토리얼 도움을 받아 구현 가능
- 개념은 대부분 설명 가능

### C 이하

- 코드를 따라 쳤지만 구조를 설명하지 못함
- 프로젝트가 특정 환경에서만 우연히 실행됨

---

# 7. 가장 중요한 진행 규칙

## 1. 선수과목 때문에 프로젝트를 멈추지 않는다

필요한 개념이 나오면 해당 부분만 먼저 학습한다.

```text
문제 발생
↓
필요한 C++ / OS / ML 개념 확인
↓
문헌 공부
↓
작은 실습
↓
Isaac 프로젝트로 복귀
```

---

## 2. Randomization보다 baseline이 먼저다

```text
ML:
확률/고전 ML
↓
PyTorch / Deep Learning

RL:
MDP / value / policy
↓
policy gradient / PPO

Isaac:

nominal environment
↓
PD baseline
↓
deterministic disturbance
↓
domain randomization
↓
RL nominal
↓
RL randomized
```

이 순서를 지킨다.

---

## 3. RL이 목적이 아니다

목적은 **로봇 시스템을 이해하고 비교 가능한 실험을 설계하는 것**이다.

PD가 RL보다 좋게 나와도 실패가 아니다.

---

## 4. 튜토리얼 완료보다 구현 능력이 중요하다

다음 질문에 답할 수 있어야 완료로 본다.

> 문서를 닫고도 내가 이걸 다시 만들 수 있는가?

---

## 5. 최종 목표

16주 종료 시 다음 문장을 실제 결과물로 증명한다.

> 나는 C++로 시스템 코드를 작성하고, OS의 thread/synchronization/timing을 이해하며, 고전 머신러닝의 회귀·분류·확률적 추정·regularization·PCA·SVM의 핵심을 설명하고, PyTorch 기반 딥러닝과 RL/PPO의 기본 구조를 이해하며, Isaac Sim/Isaac Lab에서 로봇 환경을 구성해 baseline control, disturbance, domain randomization, reinforcement learning을 적용하고 정량적으로 비교할 수 있다.

# [FOR DEMO] SDI CI/CD PIPELINE EXAMPLE 
[![en](https://img.shields.io/badge/Lang-en-green.svg)](./README.en.md) ![license](https://img.shields.io/badge/License-MIT-blue.svg)

SDI 1차년도 CI/CV/CD 파이프라인 데모를 위한 예제 저장소입니다.

범위:
개발자가 소스를 개발하거나 요구사항을 push --> 요구사항 분석(kaist) --> Nodes 선정(kaist) --> List of Nodes 생성(kaist) --> Container 패키징(jenkins) --> 맞춤형 container 생성(output)


---
## TODO 
 * 프로젝트 README TOC 만들기
 * 틈틈히 소스코드 및 README 작성하기
 * list_of_nodes 의 파일 형식 및 형태 정하기
 * Container 경량화 문제 다루기
---
## Table of Contents


## Overview
![overview](./docs/images/overview.jpg)


## Conventions
### Branch strategy
본 저장소는 Git-flow전략을 이용해 브랜치를 관리합니다.

`main(master)`: 오류없이 배포할 수 있도록 완성된 브랜치

`develop`: `main`브랜치 기반으로 다음 버전을 개발하는 브랜치

`release`: 다음 배포 버전을 준비하는 브랜치 (`develop` 브랜치에서 작업중인 기능이 완성/검증되면 `release`로 merge 됩니다.)

`feature`: 작은 모듈 및 기능을 개발하기 위한 브랜치

`hotfix`: 버그 수정을 위한 브랜치

관련해 읽어보면 도움이 되는 블로그입니다: [우린 Git-flow를 사용하고 있어요
](https://techblog.woowahan.com/2553/)

### ROS2 node naming
TBD


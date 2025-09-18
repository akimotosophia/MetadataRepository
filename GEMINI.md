# Gemini コードアシスタント用コンテキスト

このファイルは、Geminiコードアシスタントがプロジェクトを理解し、より関連性の高い、正確なサポートを提供するためのコンテキスト情報を提供します。

## プロジェクト概要

企業のデータ基盤におけるメタデータを管理するためのDB及び画面を持つシステムです。保守性と開発生産性を重視し、モダンで主流な技術を選定しています。

*   **目的:** 企業のデータ資産の可視性と管理性を向上させるためのメタデータ管理システムのMVP（Minimum Viable Product）を開発する。
*   **主要技術:**
    *   **バックエンド:** Python, FastAPI
    *   **フロントエンド:** React (TypeScript)
    *   **データベース:** PostgreSQL
    *   **コンテナ技術:** Docker, Docker Compose
*   **アーキテクチャ:** FastAPIによるAPIサーバー、Reactによるフロントエンド、PostgreSQLデータベースで構成される3層アーキテクチャ。開発・実行環境としてDockerおよびDocker Composeを使用し、コンテナベースでの開発を目指します。

## ビルドと実行

*   **前提条件:**
    *   Docker
    *   Docker Compose
*   **イメージのビルド:**
    ```bash
    docker-compose build
    ```
*   **アプリケーションの起動:**
    ```bash
    docker-compose up
    ```
    *   フロントエンド: `http://localhost:3000`
    *   バックエンドAPI Docs: `http://localhost:8000/docs`
*   **アプリケーションの停止:**
    ```bash
    docker-compose down
    ```
*   **テストの実行:**
    *   バックエンド: `docker-compose exec backend pytest`
    *   フロントエンド: `docker-compose exec frontend npm test`

## 開発規約

*   **コーディングスタイル:**
    *   **バックエンド:** Black (フォーマッタ), isort (インポート順序), Ruff (リンター)
    *   **フロントエンド:** Prettier (フォーマッタ), ESLint (リンター)
*   **テストプラクティス:**
    *   **バックエンド:** Pytestを用いたユニットテスト・結合テストを記述する。
    *   **フロントエンド:** Jest, React Testing Libraryを用いたコンポーネントテストを記述する。
*   **コントリビューションガイドライン:** (TODO: チームのルールに合わせて記述してください。)

*   **コミットメッセージ規約:**
    [Conventional Commits](https://www.conventionalcommits.org/ja/v1.0.0/) を採用します。
    フォーマット: `<type>(<scope>): <description>`
    *   `<type>` (必須): コミットの種類 (例: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `build`, `ci`, `perf`)
    *   `<scope>` (任意): 変更が影響する範囲 (例: `backend`, `frontend`, `docker`)
    *   `<description>` (必須): 変更内容の簡潔な説明

## 主要なファイル構成

*   `docker-compose.yml`: 開発環境全体の構成管理
*   `backend/Dockerfile`: バックエンドのコンテナ定義
*   `backend/app/main.py`: FastAPIアプリケーションのエントリポイント
*   `frontend/Dockerfile`: フロントエンドのコンテナ定義
*   `frontend/src/App.tsx`: Reactアプリケーションのメインコンポーネント

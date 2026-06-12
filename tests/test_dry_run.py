# -*- coding: utf-8 -*-
"""Tests for --dry-run parameter functionality."""

import pytest
from unittest.mock import patch, AsyncMock
import asyncio

import config
from cmd_arg.arg import parse_cmd


class TestDryRunConfig:
    """Test DRY_RUN configuration defaults."""

    def test_dry_run_default_false(self):
        """Test DRY_RUN default value is False."""
        from config.base_config import DRY_RUN
        assert DRY_RUN is False


class TestDryRunParsing:
    """Test --dry-run argument parsing."""

    @pytest.mark.asyncio
    async def test_dry_run_yes(self):
        """Test --dry-run yes is parsed as True."""
        args = await parse_cmd(["--platform", "tieba", "--dry-run", "yes"])
        assert args.dry_run is True

    @pytest.mark.asyncio
    async def test_dry_run_true(self):
        """Test --dry-run true is parsed as True."""
        args = await parse_cmd(["--platform", "tieba", "--dry-run", "true"])
        assert args.dry_run is True

    @pytest.mark.asyncio
    async def test_dry_run_1(self):
        """Test --dry-run 1 is parsed as True."""
        args = await parse_cmd(["--platform", "tieba", "--dry-run", "1"])
        assert args.dry_run is True

    @pytest.mark.asyncio
    async def test_dry_run_no(self):
        """Test --dry-run no is parsed as False."""
        args = await parse_cmd(["--platform", "tieba", "--dry-run", "no"])
        assert args.dry_run is False

    @pytest.mark.asyncio
    async def test_dry_run_false(self):
        """Test --dry-run false is parsed as False."""
        args = await parse_cmd(["--platform", "tieba", "--dry-run", "false"])
        assert args.dry_run is False

    @pytest.mark.asyncio
    async def test_dry_run_0(self):
        """Test --dry-run 0 is parsed as False."""
        args = await parse_cmd(["--platform", "tieba", "--dry-run", "0"])
        assert args.dry_run is False

    @pytest.mark.asyncio
    async def test_dry_run_default(self):
        """Test default value when --dry-run not specified."""
        args = await parse_cmd(["--platform", "tieba"])
        assert args.dry_run is False

    @pytest.mark.asyncio
    async def test_dry_run_updates_config(self):
        """Test that --dry-run updates config.DRY_RUN."""
        with patch.object(config, 'DRY_RUN', False):
            await parse_cmd(["--platform", "tieba", "--dry-run", "yes"])
            assert config.DRY_RUN is True


class TestDryRunExecution:
    """Test dry-run execution behavior."""

    @pytest.mark.asyncio
    async def test_dry_run_prints_config(self, capsys):
        """Test dry-run mode prints configuration."""
        with patch.object(config, 'DRY_RUN', True), \
             patch.object(config, 'PLATFORM', 'tieba'), \
             patch.object(config, 'CRAWLER_TYPE', 'search'), \
             patch.object(config, 'LOGIN_TYPE', 'qrcode'), \
             patch.object(config, 'KEYWORDS', '测试关键词'), \
             patch.object(config, 'START_PAGE', 1), \
             patch.object(config, 'CRAWLER_MAX_NOTES_COUNT', 5), \
             patch.object(config, 'ENABLE_GET_COMMENTS', True), \
             patch.object(config, 'ENABLE_GET_SUB_COMMENTS', False), \
             patch.object(config, 'SAVE_DATA_OPTION', 'jsonl'), \
             patch.object(config, 'SAVE_DATA_PATH', ''), \
             patch.object(config, 'HEADLESS', False), \
             patch.object(config, 'ENABLE_IP_PROXY', False), \
             patch.object(config, 'MAX_CONCURRENCY_NUM', 1), \
             patch.object(config, 'CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES', 10), \
             patch('sys.argv', ['main.py', '--platform', 'tieba', '--dry-run', 'yes']):

            from main import main
            await main()

            captured = capsys.readouterr()
            assert "[DRY-RUN] MediaCrawler Configuration Preview" in captured.out
            assert "Platform:           tieba" in captured.out
            assert "Crawler Type:       search" in captured.out
            assert "Keywords:           测试关键词" in captured.out
            assert "[DRY-RUN] No browser launched" in captured.out

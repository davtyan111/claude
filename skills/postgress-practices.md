Supabase Postgres Best Practices
Editor's Note
A solid reference for anyone working with Postgres, especially on Supabase. Contains 8 categories of performance rules prioritized by impact, from critical query optimization to advanced features. Each rule includes wrong vs. right SQL examples, query plan analysis, and specific performance metrics. The prioritization system is smart - it focuses on the stuff that actually breaks production first (missing indexes, connection pooling) before getting into nice-to-haves. Worth having loaded when reviewing database code or designing schemas, since it catches common Postgres pitfalls that can tank performance.

Install
npx skills add https://github.com/supabase/agent-skills --skill supabase-postgres-best-practices

SKILL.md
Supabase Postgres Best Practices
Comprehensive performance optimization guide for Postgres, maintained by Supabase. Contains rules across 8 categories, prioritized by impact to guide automated query optimization and schema design.

When to Apply
Reference these guidelines when:

Writing SQL queries or designing schemas
Implementing indexes or query optimization
Reviewing database performance issues
Configuring connection pooling or scaling
Optimizing for Postgres-specific features
Working with Row-Level Security (RLS)
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Query Performance	CRITICAL	query-
2	Connection Management	CRITICAL	conn-
3	Security & RLS	CRITICAL	security-
4	Schema Design	HIGH	schema-
5	Concurrency & Locking	MEDIUM-HIGH	lock-
6	Data Access Patterns	MEDIUM	data-
7	Monitoring & Diagnostics	LOW-MEDIUM	monitor-
8	Advanced Features	LOW	advanced-
How to Use
Read individual rule files for detailed explanations and SQL examples:

references/query-missing-indexes.md
references/query-partial-indexes.md
references/_sections.md
Each rule file contains:

Brief explanation of why it matters
Incorrect SQL example with explanation
Correct SQL example with explanation
Optional EXPLAIN output or metrics
Additional context and references
Supabase-specific notes (when applicable)
References
https://www.postgresql.org/docs/current/
https://supabase.com/docs
https://wiki.postgresql.org/wiki/Performance_Optimization
https://supabase.com/docs/guides/database/overview
https://supabase.com/docs/guides/auth/row-level-security
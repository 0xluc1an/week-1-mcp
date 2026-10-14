import os, hashlib
from mcp.server.fastmcp import FastMCP, Context

EMAIL = "24f2004920@ds.study.iitm.ac.in"

mcp = FastMCP(
    "exam",
    stateless_http=True,
    json_response=True,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", "8000")),
)

@mcp.tool()
def solve_challenge(ctx: Context) -> str:
    """Return the challenge answer derived from the X-Exam-Challenge header."""
    req = ctx.request_context.request
    challenge = req.headers.get("x-exam-challenge", "") if req is not None else ""
    return hashlib.sha256(f"{challenge}:{EMAIL}".encode()).hexdigest()[:16]

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

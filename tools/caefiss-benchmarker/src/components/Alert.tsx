/*
    Alert: text-fg-brand-strong; bg-brand-softer
    Danger: text-fg-danger-strong; bg-danger-soft 
    Success: text-fg-success-strong; bg-success-soft
    Warning: text-fg-warning; bg-warning-soft
    Regular: text-heading; bg-neutral-secondary-medium
*/

function Alert({
  color,
  bgColor,
  message,
}: {
  color: string;
  bgColor: string;
  message: string;
}) {
  return (
    <>
      <div
        className={`animate-slide-in flex items-start sm:items-center p-4 mb-4  w-100 text-sm ${color} text-blue-300 rounded-xl ${bgColor} transition-all duration-500 ease-in-out`}
        role="alert"
      >
        <svg
          className="w-4 h-4 me-2 shrink-0 mt-0.5 sm:mt-0"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          fill="none"
          viewBox="0 0 24 24"
        >
          <path
            stroke="currentColor"
            strokeLinecap="round"
            strokeWidth="2"
            d="M10 11h2v5m-2 0h4m-2.592-8.5h.01M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
          />
        </svg>
        <p>{message}</p>
      </div>
    </>
  );
}

export default Alert;
